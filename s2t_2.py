
import speech_recognition as sr

r=sr.Recognizer()

f='D:\\dell\\Documents\\Sound recordings\\Recording.wav'

with sr.AudioFile(f) as source:
    audio=r.record(source)
    print(r.recognize_google(audio))