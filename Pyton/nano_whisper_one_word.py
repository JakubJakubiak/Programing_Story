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
    model = whisper.load_model("small")
    audio = whisper.load_audio("video.webm")
    output_path = 'output.srt'

    transcriptions = []
    resulty = model.transcribe(audio, verbose=True)
   
    for i, segment in enumerate(resulty["segments"]):
        start_time = segment["start"]
        end_time = segment["end"]
        words = segment["text"].split()
        print(segment["text"])

        total_characters = sum(len(word) for word in words)
        total_time = end_time - start_time

        line_start_time = start_time
        line_end_time = start_time

        for word in words:
            word_time = (len(word) / total_characters) * total_time
            line_end_time += word_time
            transcriptions.append(f"{i+1}\n{format_srt_time(line_start_time)} --> {format_srt_time(line_end_time)}\n{word}\n")
            line_start_time = line_end_time

        print(f"{i+1}")
        print(f"Start: {format_srt_time(start_time)}, End: {format_srt_time(end_time)}")
        print(words)
        print("-" * 40)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(transcriptions))

if __name__ == "__main__":
    main()
