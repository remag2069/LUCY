import webbrowser as wb
import speech_recognition as  sr
import re
import datetime as dt
from suppliments import voice_pa as v
from suppliments import keyboard_input
import os
import time

kas=0
reset_time=5
current_time=time.localtime(time.time())[4]
reset_time=(reset_time+current_time)
r=sr.Recognizer()
'''
def google_code(terms):
    terms.replace('/n','')
    print(terms)
    temp=re.split('~',terms)
    t=[]
    for i in temp:
        t.append(re.split('/',i))
'''
    



def recon(l,text):
    for i in l:
        if i in text:
            return True


#search::
def search(text):
    print(text)
    s=''
    spl=text.split()
    for i in range(len(spl)):
        if(spl[i]=='search'):
            s=spl[i+1:]
    st=''            
    #print(s)
    for i in s:
        st=st+i+'+'
    st=st[:-1]
    #print(st)

    url='https://www.google.com/search?q='+st+'&rlz=1C1CHBF_enIN854IN854&oq='+st+'&aqs=chrome.1.69i57j69i59l2j0l3.4673j0j7&sourceid=chrome&ie=UTF-8'
    #print('searching for \''+s+'\'')
    wb.open(url)
#time
def Ret_time():
    print('today\'s date and time are:')
    print(dt.datetime.now())
#bye
def bye():
    print('bye')
    v.hi()
    exit()
#go
def go(text):
    if 'control panel' in text:
        print('Acessing control panel')
        os.system('Control.exe')
    elif 'moodle' in text:
        print('Acessing Moodle')
        wb.open('https://moodle.iitb.ac.in/login/index.php')
    elif 'YouTube' in text:
        print('playing youtube')
        wb.open('https://www.youtube.com/')
    else:
        print('\'open\' function works with \n1.control panel\n2.moodle')
    m=open('D:\\python projects\\speechtotext\\pa name\\music.txt')
    music_var=re.split('/',m.read())
    m.close()

    if recon(music_var,text):
        print('playing music')
        os.system('.\\apps\\groove\\groove.bat')


#end
def end(text):
    m=open('D:\\python projects\\speechtotext\\pa name\\music.txt')
    music_var=re.split('/',m.read())
    m.close()

    if recon(music_var,text):
        os.system('.\\apps\\groove\\end_groove.bat')


#help
def help():
    print('Available functions and their key words:')
    print('Activation:\n\'lucy\'')
    print('Search on WEB:\n\'search\'')
    print('Time:\n\'time\'')
    print('Open apps:\n\'open\'')
    print('Deactivation:\n\'bye\'')
#search_this
def search_this():
    print('searching...')
    search_term=keyboard_input.keyboard_read()
    search_term='search '+search_term
    search(search_term)



#Execute
def execute(text):
    global kas
    v.hiO(text)
    kas=kas+1
    print(kas)
    print('yes sir, i am listening')
    with sr.Microphone() as source:
    #print('setting up ...')
        r.adjust_for_ambient_noise(source,duration=0.1)
            
        try:
            audio=r.listen(source,timeout=2,phrase_time_limit=15)
            text=r.recognize_google(audio)
        except:
            print('')
            return
        
    #search_this
    f=open('D:\\python projects\\speechtotext\\pa name\\search_this.txt')
    t=f.read()
    f.close()
    t=re.split('/',t)
    if recon(t,text):
        print(text)
        search_this()
        return

    #search
    if 'search' in text:
        search(text)
        return
    #time
    f=open('D:\\python projects\\speechtotext\\pa name\\time.txt')
    t=f.read()
    f.close()
    t=re.split('/',t)
    if recon(t,text):
        print(text)
        Ret_time()
        return
    #go
    f=open('D:\\python projects\\speechtotext\\pa name\\go.txt')
    t=f.read()
    f.close()
    t=re.split('/',t)
    if recon(t,text):
        go(text)
        return
    #end
    f=open('D:\\python projects\\speechtotext\\pa name\\end.txt')
    t=f.read()
    f.close()
    t=re.split('/',t)
    if recon(t,text):
        end(text)
        return



def reset():
    # v.hi()
    # v.hi()
    os.system('.\\apps\\LUCY.bat')
    exit()

'''     
with sr.Microphone() as source:
    print('setting up ...')
    r.adjust_for_ambient_noise(source,duration=3)
    print('listening')
    #audio=r.listen(source)
'''
'''
try:
    text=r.recognize_google(audio)
except:
    print('')
'''


with sr.Microphone() as source:
    #print('setting up ...')
    r.adjust_for_ambient_noise(source,duration=3)
    while(True):
        print('a')
        C_time=time.localtime(time.time())[4]
        print(reset_time-C_time)
        try:
            print('b')
            audio=r.listen(source,timeout=1,phrase_time_limit=3)
            print('A')        
            text=r.recognize_google(audio)
            print(text)
        except:
            print('')
            if int(C_time)>=reset_time:
                reset()
            continue
        #bye
        b=open('D:\\python projects\\speechtotext\\pa name\\bye.txt','r')
        bye_var=re.split('/',b.read())  
        b.close()  
        if recon(bye_var,text):
            #print("goodbye sir")
            bye()
            break
        
        #Activation
        n=open('D:\\python projects\\speechtotext\\pa name\\name.txt','r')
        name=re.split('/',n.read())
        if recon(name,text):
            execute(text)
        '''else:
            f=open('D:\\python projects\\speechtotext\\pa name\\yes.txt','a')
            f.write(text)
            f.write('/')
            f.close()
        '''
        n.close()

        #Restart
        r_var=open('D:\\python projects\\speechtotext\\pa name\\restart.txt','r')
        restart=re.split('/',r_var.read())
        r_var.close()
        if recon(restart,text) or int(C_time)>=reset_time:
            reset()

        #help
        if 'help' in text:
            help()

    

