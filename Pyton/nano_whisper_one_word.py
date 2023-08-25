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
    audio = whisper.load_audio("PRZEKLĘTY PACZKOMAT.webm")
    output_path = 'output.srt'

    transcriptions = []
    resulty = model.transcribe(audio, fp16=False)

    for i, segment in enumerate(resulty["segments"]):
        start_time = format_srt_time(segment["start"])
        end_time = format_srt_time(segment["end"])
        words = segment["text"].split()

        line_start_time = segment["start"]
        line_end_time = segment["start"] + (segment["end"] - segment["start"]) / len(words)

        for j, word in enumerate(words):
            transcriptions.append(f"{i+1}\n{format_srt_time(line_start_time)} --> {format_srt_time(line_end_time)}\n{word}\n")
            line_start_time = line_end_time
            line_end_time = segment["start"] + ((j + 2) * (segment["end"] - segment["start"]) / len(words))

        print(f"{i+1}")
        print(f"Start: {start_time}, End: {end_time}")
        print(words)
        print("-" * 40)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(transcriptions))

if __name__ == "__main__":
    main()
