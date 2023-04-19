import asyncio
from logging import root
import os
import aiohttp

import tkinter as tk
from tkinter import messagebox
from tqdm import tqdm


from ttkthemes import ThemedTk
from tkinter import ttk

# async def download_image(url, file_name):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             if response.status == 200:
#                 with open(os.path.join("png", file_name), "wb") as f:
#                     image_data = await response.read()
#                     f.write(image_data)
#                     print(f"Image {file_name} was downloaded and saved in the images folder.")
#             else:
#                 print(f"Failed to download image from address {url}.")

# async def main():

#     images_urls_no_duuplikate = [     
#   'https://cdn.midjourney.com/dd13b648-12d4-4546-b8be-48d771079db1/grid_0_640_N.webp',
#   'https://cdn.midjourney.com/7e00f9e4-b80b-4a62-ac0a-3697e0d7aad1/grid_0_640_N.webp',
# #   'https://cdn.midjourney.com/86fc0219-f371-4f79-9c5a-ad331820a131/grid_0_640_N.webp',
# #   'https://cdn.midjourney.com/0bae794f-2401-41a0-9abd-8c79c58a7cc3/grid_0_640_N.webp',
# #   'https://cdn.midjourney.com/f56ec7b2-48c1-47d4-90f0-84660540d469/grid_0_640_N.webp',
# ]


    

#     image_urls = list(set(images_urls_no_duuplikate))

#     os.makedirs("png", exist_ok=True)
#     tasks = []
#     for i, url in enumerate(image_urls):
#         file_name = f"image_{i+1}_{url.split('/')[-1]}"   
        
#         if os.path.exists(os.path.join("png", file_name)):
#             print(f"Image {file_name} already exists.")
#         else:
#             task = asyncio.ensure_future(download_image(url, file_name))
#             tasks.append(task)
#     await asyncio.gather(*tasks)

# if __name__ == "__main__":
#     asyncio.run(main())

# /////////////////////////////////////////////////////////////////////////////////////////


# def add_url():
#     url = url_entry.get()
#     if url:
#         images_urls_no_duuplikate.append(url)
#         url_entry.delete(0, tk.END)
#         messagebox.showinfo("Success", "URL added to list.")
#     else:
#         messagebox.showerror("Error", "Please enter a valid URL.")

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

    images_urls_no_duuplikate = [     
  'https://cdn.midjourney.com/dd13b648-12d4-4546-b8be-48d771079db1/grid_0_640_N.webp',
  'https://cdn.midjourney.com/7e00f9e4-b80b-4a62-ac0a-3697e0d7aad1/grid_0_640_N.webp',
#   'https://cdn.midjourney.com/86fc0219-f371-4f79-9c5a-ad331820a131/grid_0_640_N.webp',
#   'https://cdn.midjourney.com/0bae794f-2401-41a0-9abd-8c79c58a7cc3/grid_0_640_N.webp',
#   'https://cdn.midjourney.com/f56ec7b2-48c1-47d4-90f0-84660540d469/grid_0_640_N.webp',
]


    




# async def download_image(url, file_name):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             if response.status == 200:
#                 with open(os.path.join("png", file_name), "wb") as f:
#                     async for data in tqdm(response.content.iter_chunked(1024),
#                                            desc=file_name, unit='B',
#                                            unit_scale=True, unit_divisor=1024):
#                         f.write(data)
#                     print(f"Image {file_name} was downloaded and saved in the images folder.")
#             else:
#                 print(f"Failed to download image from address {url}.")

# images_urls_no_duuplikate=['https://cdn.pixabay.com/photo/2020/11/01/21/44/angel-5705040__480.jpg']



    image_urls = list(set(images_urls_no_duuplikate))

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
    



    with tqdm(total=len(tasks), desc="Downloading Images") as pbar:
        for task in tasks:
            await task
            pbar.update(1)

    progress_listbox = tk.Listbox(root)
    progress_listbox.pack()
    for url in images_urls_no_duuplikate:
        progress_listbox.insert(tk.END, url)
    def add_url():
     url = url_entry.get()
    if url:
        images_urls_no_duuplikate.append(url)
        url_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "URL added to list.")
    else:
        messagebox.showerror("Error", "Please enter a valid URL.")

    root = tk.Tk()
    root.title("Image Downloader")



    frame = tk.Frame(root)
    frame.pack()

    url_label = tk.Label(frame, text="Enter URL:")
    url_label.pack(side=tk.LEFT)
    root.geometry("800x600")
    url_entry = tk.Entry(frame)
    url_entry.pack(side=tk.LEFT)
    add_button = tk.Button(frame, text="Add", command=add_url)
    add_button.pack(side=tk.LEFT)
    download_button = tk.Button(root, text="Download", command=main)
    download_button.pack()
    with tqdm(total=len(tasks), desc="Downloading Images", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        url_entry = ttk.Entry(frame, width=50, textvariable=url_var)
    url_entry.insert(0, "Enter url")

    root.mainloop()

if __name__ == "__main__":
    asyncio.run(main())



# async def main():
#     os.makedirs("png", exist_ok=True)
#     tasks = []
#     for i, url in enumerate(images_urls_no_duuplikate):
#         file_name = f"image_{i+1}_{url.split('/')[-1]}"   
#         if os.path.exists(os.path.join("png", file_name)):
#             print(f"Image {file_name} already exists.")
#         else:
#             task = asyncio.ensure_future(download_image(url, file_name))
#             tasks.append(task)

#     with tqdm(total=len(tasks), desc="Downloading Images") as pbar:
#         for task in tasks:
#             await task
#             pbar.update(1)
        
#     progress_listbox = tk.Listbox(root)
#     progress_listbox.pack()
#     for url in images_urls_no_duuplikate:
#         progress_listbox.insert(tk.END, url)


# def add_url():
#     url = url_entry.get()
#     if url:
#         images_urls_no_duuplikate.append(url)
#         url_entry.delete(0, tk.END)
#         messagebox.showinfo("Success", "URL added to list.")
#     else:
#         messagebox.showerror("Error", "Please enter a valid URL.")

# root = tk.Tk()
# root.title("Image Downloader")



# frame = tk.Frame(root)
# frame.pack()

# url_label = tk.Label(frame, text="Enter URL:")
# url_label.pack(side=tk.LEFT)
# root.geometry("800x600")

# url_entry = tk.Entry(frame)
# url_entry.pack(side=tk.LEFT)

# add_button = tk.Button(frame, text="Add", command=add_url)
# add_button.pack(side=tk.LEFT)

# download_button = tk.Button(root, text="Download", command=main)
# download_button.pack()

# with tqdm(total=len(tasks), desc="Downloading Images", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
#     url_entry = ttk.Entry(frame, width=50, textvariable=url_var)
# url_entry.insert(0, "Enter url")


# root.mainloop()
