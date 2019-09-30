'''

import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print('say')
    audio=r.listen(source)
try:
    text=r.recognize_google(audio)
    print(text)
except:
    print('error')

'''

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone() as source:
    print('setting up ....')
    r.adjust_for_ambient_noise(source, duration=2)
    print("Say something!")
    audio = r.listen(source)

print(r.recognize_google(audio))
