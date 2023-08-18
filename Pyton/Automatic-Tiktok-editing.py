from moviepy.editor import VideoFileClip, clips_array,CompositeVideoClip
import os
import subprocess

path_up = './Video_up/'     # Folder with video files for the upper part
path_down = './Video_down/' # Folder with video files for the lower part
path_out = './Output/'      # Folder to save edited videos

# Create the output folder if it doesn't exist
os.makedirs(path_out, exist_ok=True)

up_filenames = os.listdir(path_up)
down_filenames = os.listdir(path_down)

for up_filename, down_filename in zip(up_filenames, down_filenames):
    up_video = VideoFileClip(os.path.join(path_up, up_filename))
    down_video = VideoFileClip(os.path.join(path_down, down_filename))
    
    up_duration = up_video.duration
    down_duration = down_video.duration
    
    combined_duration = min(up_duration, down_duration)
    
    up_video = up_video.subclip(0, combined_duration)
    down_video = down_video.subclip(0, combined_duration)
    
    # Resize the clips to 50% and arrange them vertically
    up_video = up_video.resize(height=up_video.h // 2, width=up_video.w)
    down_video = down_video.resize(height=down_video.h //2 , width=down_video.w)

    down_video = down_video.crop(x1=0, y1=100, x2=720, y2=550)
    down_video = down_video.set_audio(None)
    
    
    combined = clips_array([[up_video], [down_video]])
    
    clean_name = os.path.splitext(up_filename)[0]
    output_path = os.path.join(path_out, f'{clean_name}_combined.mp4')
    combined.write_videofile(output_path, threads=4)  # Use GPU acceleration

    ffmpeg_command = [
        "ffmpeg",
        "-hwaccel", "cuda",
        "-i", output_path,
        "-c:v", "h264_nvenc",  
    ]

    subprocess.run(ffmpeg_command)
