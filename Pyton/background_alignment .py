from PIL import Image
import numpy as np
import os


input_folder = "./image_not_equal "
output_folder = "./images"

#distance from background 
distance = 1.2  # 1.1, 1.2, 1.3, 1.4, 1.5 
size_image = 600 

for filename in os.listdir(input_folder):
    if filename.endswith(".webp") or filename.endswith(".png") or filename.endswith(".jpg"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        new_size=0
        new_img_width, new_img_height = img.size
        

        if new_img_width >= new_img_height:
            new_size = int(new_img_width*distance)
        else:
            new_size = int(new_img_height*distance)

        new_img = Image.new("RGB", (new_size, new_size), (255, 255, 255))

        x_offset = (new_img.width - img.width) // 2
        y_offset = (new_img.height - img.height) // 2
        new_img.paste(img, (x_offset, y_offset))

        new_img.thumbnail((size_image, size_image))

        # Save the image with a new name in the output folder
        output_filename = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(output_folder, output_filename)
        new_img.save(output_path)
        print(f"save {output_filename}")

print("Conversion complete.")