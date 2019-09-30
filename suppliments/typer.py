'''
from pynput.keyboard import Key,Controller
import time
import speech_recognition as s


def type():
    time.sleep(3)
    k=Controller()
    r=s.Recognizer()
    ch=1
    while (ch==1):
        with s.Microphone() as source:
            try:
                audio=r.listen(source,phrase_time_limit=10)
                text=r.recognize_google(audio)
            except:
                pass
        k.type(text)
        if k.p




'''
ch=1
repeat=0
text=''

import time
import speech_recognition as s
import pynput.keyboard as k
import threading as t
import re

def typer():
    global text
    print('hi')
    time.sleep(3)
    cont=k.Controller()
    r=s.Recognizer()
    #ch=1
    with s.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=3)
        while (ch==1):
            try:
                print('listening')
                audio=r.listen(source)
                text=text + r.recognize_google(audio)
                print(text)
                
            except:
                pass
            
        
def writer():
    global text
    while ch==1:
        #print('typing')
        #print(text)
        cont=k.Controller()
        cont.type(text)
        text=''


#key=k.Controller
def quiter():
    def on_press(key):
        pass
        #print(key)
    #        n=-1
    def on_release(key):
        if(key==k.Key.esc):
            print('exit')
            #t1.stop()
            global ch
            ch=0
            #print(ch)
            #ch=0
            #print(ch)
            return False

    #print('a')
    with k.Listener(on_press=on_press,on_release=on_release) as l:
        l.join()
        #print('quit')

            #l.stop()
        #if key.shift_pressed():
        # exit()

def run():
    t1=t.Thread(target=typer)

    t2=t.Thread(target=quiter)
    t3=t.Thread(target=writer)
    t1.start()
    t2.start()
    t3.start()

    #print(t1.is_alive())
    #print(t2.is_alive())
    #time.sleep(5)
    #print(t1._is_stopped)
    #print(t2._is_stopped)
    #if not t2.is_alive() :
        #print(t1._is_stopped)
        #t1._delete()
        #print(t1._is_stopped)
    #print('end')
run()





'''
import time
import speech_recognition as s
import pynput.keyboard as k
import threading as t

def quitter():
    def on_press(key):
        print(key)

    def on_release(key):
        if key==k.Key.esc:
            return False

    with k.Listener(on_press=on_press,on_release=on_release) as l:
        l.join()

def hearer():
    n=100
    while(n>0):
        print('hi')
        n=n-1
t1=t.Thread(target=quitter)
#t1.start()
t2=t.Thread(target=hearer)
t2.start()
print('reached')
#time.sleep(5)
t2._delete()


'''