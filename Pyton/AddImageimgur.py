from imgurpython import ImgurClient
import os
import json
import asyncio

client_id = ''
client_secret = ''

client = ImgurClient(client_id, client_secret)

folder_path = 'output_folder/'
image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.jpg', '.png', '.gif'))]

uploaded_links = []

async def upload_image(image_path):
    response = client.upload_from_path(image_path)
    
    if response:
        uploaded_links.append({
            "link": response['link'],
        })
    else:
        print(f'An error occurred while uploading the image {image_path}')

async def main():
    tasks = [upload_image(image_path) for image_path in image_paths]
    await asyncio.gather(*tasks)

print('Image transfer has begun.')
asyncio.run(main())
print('Uploading of images has been completed.')

with open('links.json', 'w') as linki_file:
    json.dump(uploaded_links, linki_file, indent=4)

print('Links stored in links.json file.')