import pynput
from pynput.keyboard import Key
import time
import threading
import win32clipboard as w

def keyboard_read():
    time.sleep(1)
    k=pynput.keyboard.Controller()
    k.press(Key.ctrl)
    k.press('c')
    print('c')
    k.release(Key.ctrl)
    k.release('c')
    print('taken')
    time.sleep(1)
    w.OpenClipboard()
    v=w.GetClipboardData()
    w.EmptyClipboard()
    w.CloseClipboard()
    print(v)
    return v

