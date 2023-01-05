from moviepy import *
from moviepy.editor import *
import os

path = './video/' #folder with video for editing
pathOut = '/editVideo'

for filename in os.listdir(path):
    video1 = VideoFileClip(f"{path}/{filename}").subclip(10,20)
    video2 = VideoFileClip(f"{path}/{filename}").subclip()
    combined = clips_array([[video1,video2]])
    clean_name = os.path.splitext(filename)[0]
    combined.write_videofile(f'.{pathOut}/{clean_name}_edited.mp4')