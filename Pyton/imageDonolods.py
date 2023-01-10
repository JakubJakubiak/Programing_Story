import asyncio
import os
import aiohttp

async def download_image(url, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(os.path.join("png", file_name), "wb") as f:

                    image_data = await response.read()
                    f.write(image_data)
                    print(f"Image {file_name} was downloaded and saved in the images folder.")
            else:
                print(f"Failed to download image from address {url}.")

async def main():

    image_urls = [
  'https://cdn.midjourney.com/a1a79d61-2ebd-4b04-a269-a5ab4614f0db/grid_0_640_N.webp',
  'https://cdn.midjourney.com/c644780e-759c-44de-b989-8eb38c052c98/grid_0_640_N.webp',
  'https://cdn.midjourney.com/2b41197d-894f-4429-b0ad-60ed0ebcdcbd/grid_0_640_N.webp',
    ]
    
    os.makedirs("png", exist_ok=True)
    tasks = []
    for i, url in enumerate(image_urls):
        file_name = f"image_{i+1}_{url.split('/')[-1]}"   
        
        if os.path.exists(os.path.join("png", file_name)):
            print(f"Image {file_name} already exists.")
        else:
            task = asyncio.ensure_future(download_image(url, file_name))
            tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())


