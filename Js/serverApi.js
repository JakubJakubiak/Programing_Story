// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import { useTextBuffer } from "nextjs-openai";
import { StreamingTextURL } from "nextjs-openai";
import { OpenAI } from "openai-streams";
import { Configuration, OpenAIApi } from "openai";
import axios, { isCancel, AxiosError } from 'axios';



export default function handler(req, res) {
  if (req.method === 'POST') {
    filtrAi(req, res);
  } else {
    res.status(200).json([{ name: 'hed Test' }])
  }
}


let filtrAi = async (req, res) => {


  if (req.body.ai == 'GPT-3') {
    await gpt3Prompt(req, res);
  } else if (req.body.ai == "replicate") {
    await imageLink(req, res);
  } else {
    console.log(req.body);
    return res.status(200).json([{ name: 'hed Test ' + ` ${req.body.name}` }])
  }
}


async function gpt3Prompt(req, res) {
  let personality = req.body.personality;
  try {
    const endpoint = "https://api.openai.com/v1/chat/completions";
    (req.body.personality=="")
      ?personality = await personalityAI(req)
      :req.body.personality = req.body.personality;
    const response = await axios.post(endpoint, {
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "system",
          content: personality,
        },
        { role: "user", content: `${req.body.name}` },
      ],
      max_tokens: 300,
      temperature: 0.4,
    }, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
      },
    });



  if (response.data.choices[0].finish_reason=="stop"){
    return res.status(200).json({ success: true, data: response.data.choices[0].message.content});
  }else{
    return res.status(200).json({ success: true, data: 'error'});
  }

  } catch (error) {
    console.error(error);
    return res.status(500).json({
      success: false,
      message: "There was an error in the Prompt function",
    });
  }
}





async function personalityAI(req) {
  if (req.body.personality == "woman") {

    return `Based on the context of our conversation so far: [${JSON.stringify(req.body.history)}] Answer the question below as truthfully as you can, if you don’t know the answer, say you don’t know in a sarcastic way otherwise, just answer I don't know the answer to ${req.body.name}. It responds in the language in which it is written to you by User.`

  } else if (req.body.personality == "Bot"){
    return `You are a helpful Bot. The current story of the conversation looks like this: [${JSON.stringify(req.body.history)}] `
  }
  

  else {
    return "you are a helpful Bot";
  }
}





async function imageLink(req, res) {
  const base64Image = req.body.name;
  const url = await uploadImageToImgBB(base64Image);

  if (!url) {
    return res
      .status(500)
      .json({ reason: "Failed to upload image to ImgBB", predictionId: null });
  }
  console.log(url);

  return res.status(200).json({ success: true, data: url });
}

async function uploadImageToImgBB(base64Image) {
  const formData = new FormData();
  formData.append("image", base64Image);


  const imgbbResponse = await fetch(
    `https://api.imgbb.com/1/upload?expiration=3600&key=${process.env.IMG_API_KEY}`,
    {
      method: "POST",
      body: formData,
    }
  );

  if (!imgbbResponse.ok) {
    return null;
  }

  const jsonImgbbResponse = await imgbbResponse.json();
  const url = jsonImgbbResponse.data.url;
  return url;
}