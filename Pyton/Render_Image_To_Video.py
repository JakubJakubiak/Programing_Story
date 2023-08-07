from moviepy.editor import VideoClip, AudioFileClip, clips_array, ImageClip
from PIL import Image, ImageOps
from itertools import chain
import numpy as np
import glob

extensions = ['*.jpg*', '*.webp', '*.png']
png_files = list(chain.from_iterable(glob.glob(ext) for ext in extensions))

audioFile = "music.wav"
outputFilename = "output.mp4"

def resize_and_center_image(image, target_size):
    img_width, img_height = image.size
    target_width, target_height = target_size

    aspect_ratio = img_width / img_height
    target_aspect_ratio = target_width / target_height

    if aspect_ratio > target_aspect_ratio:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    else:
        new_height = target_height
        new_width = int(target_height * aspect_ratio)

    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    x_offset = (target_width - new_width) // 2
    y_offset = (target_height - new_height) // 2

    centered_image = Image.new("RGB", (target_width, target_height), (0, 0, 0))
    centered_image.paste(resized_image, (x_offset, y_offset))

    return centered_image

def make_frame(t):
    num = int(t * 0.25)
    img = Image.open(png_files[num])
    resized_img = resize_and_center_image(img, (576, 1024))
    img_array = np.array(resized_img)
    return img_array

video_clip = VideoClip(make_frame=make_frame, duration=AudioFileClip(audioFile).duration)
final_clip = video_clip.set_audio(AudioFileClip(audioFile))
final_clip.write_videofile(outputFilename, codec="libx264", fps=1)