import os
import whisper
import re

def format_srt_time(time):
    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    milliseconds = int((time * 1000) % 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def main():
    model = whisper.load_model("base")
    audio = whisper.load_audio("Video.webm")
    output_path = 'output.srt'

    transcriptions = []
    resulty = model.transcribe(audio, verbose=True)

    for i, segment in enumerate(resulty["segments"]):
        start_time = format_srt_time(segment["start"])
        end_time = format_srt_time(segment["end"])
        text = segment["text"]
        
        transcriptions.append(f"{i+1}\n{start_time} --> {end_time}\n{text}")
    
        print(f"{i+1}")
        print(f"Start: {start_time}, End: {end_time}")
        print(text)
        print("-" * 40)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(transcriptions))


if __name__ == "__main__":
    main()
