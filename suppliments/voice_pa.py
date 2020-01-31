import winsound as ws
import os
import time
import re

def recon(l,text):
    for i in l:
        if i in text:
            return True


def hiO(text):
    f=open('D:\\python projects\\speechtotext\\pa name\\OWK.txt')
    OWK=re.split('/',f.read())
    f.close()

    if recon(OWK,text):
        os.system('.\\suppliments\\HT.wav')
        #ws.PlaySound('HT.wav',ws.SND_ASYNC)
        #ws.Beep(3050,1000)
        time.sleep(5)
        os.system('.\\apps\\groove\\end_groove.bat')
    else:
        ws.Beep(3050,1000)
def hi():
    ws.Beep(3050,1000)