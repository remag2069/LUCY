import pynput
from pynput.keyboard import Key
import time
k=pynput.keyboard.Controller()

time.sleep(3)
k.press(Key.f6)
print('f6')

k.release(Key.f6)