import os
import requests

image_urls = [
    'https://cdn.midjourney.com/4da688fd-0085-433f-8a77-13d48a1eaeb9/grid_0_640_N.webp',
    'https://cdn.midjourney.com/d7a7d232-4c40-4151-8b10-fa8cdf76ddec/grid_0_640_N.webp',
    'https://cdn.midjourney.com/e7e9cc33-76f7-45a4-853e-8db9ba1c3b2b/grid_0_640_N.webp',
    'https://cdn.midjourney.com/307d9f1d-2fef-4dba-8066-78d45067d8c7/grid_0_640_N.webp',
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