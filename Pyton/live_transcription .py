import sounddevice as sd
import speech_recognition as sr
import threading
import wave
import os
import time

duration = 1.5  
filename = "./recorded_dark.wav"
output_text_file = "./recognized_text.txt"
running = True

def record_audio():
    print("Recording started...")
    audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
    sd.wait()
    print("Recording completed...")
    return audio_data

def save_to_wav(data, filename):
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(data.tobytes())

def recognize_speech(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="pl-PL")
            print("Recognized text:", text)
            save_text_to_file(text)
        except sr.UnknownValueError:
            print("Failed to recognize speech")
        except sr.RequestError as e:
            print("Google Speech Recognition server error; {0}".format(e))

def save_text_to_file(text):
    with open(output_text_file, 'w', encoding="utf-8") as file:
        file.write(text)

def background_recording():
    global running
    while running:
        audio_data = record_audio()
        save_to_wav(audio_data, filename)
        recognize_speech(filename)
        time.sleep(0.5)  

background_thread = threading.Thread(target=background_recording)
background_thread.start()


# time.sleep(10)

input("Press Enter to stop the program...\n")
running = False
background_thread.join()
