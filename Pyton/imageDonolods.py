import os
import requests
import asyncio

async def main():
        
    image_urls = [
    'https://cdn.midjourney.com/49ce4e9b-c8e6-406f-a568-5bbaba88ba2e/grid_0_640_N.webp',
    'https://cdn.midjourney.com/c1d742e4-283e-438e-b552-11fe12eca2a6/grid_0_640_N.webp',
    'https://cdn.midjourney.com/9dc21fb9-9415-4e31-a1ef-149d3ee98a07/grid_0_640_N.webp',
    ]

    os.makedirs("png", exist_ok=True)
    for i, url in enumerate(image_urls):
        file_name = f"image_{i+1}_{url.split('/')[-1]}"
        
        if os.path.exists(os.path.join("png", file_name)):
            file_name = file_name.split(".")[0] + "_new." + file_name.split(".")[1]
        response = requests.get(url)

        if response.status_code == 200:
            with open(os.path.join("png", file_name), "wb") as f:
                f.write(response.content)
                print(f"image {file_name} save")
        else:
            print(f"No Save {url}.")

asyncio.run(main())