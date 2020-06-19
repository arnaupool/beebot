from pynput.keyboard import Key, Controller, Listener
from threading import Thread
import time, os

keyboard = Controller()

def enum():
    for line in f.readlines():
        line = [char for char in line]
        for char in line:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(offset)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    print("--- End ---")

def on_press(key):
    if key == Key.esc:
        print("--- Quitting program ---")
        os._exit(1)

filename = input("Enter the name of the file\n")
offset = input("Enter the amount of time between keystrokes (e.g. 0.05)\n")

try:
    offset = float(offset)
except ValueError:
    print("Offset must be a floating point number\n")
    quit()

try:
    f = open(filename, 'r')
except FileNotFoundError:
    print("404")
    quit()

print("--- Starting bee sequence ---\n")
time.sleep(2)

thread = Thread(target=enum)
thread.start()

with Listener(
        on_press = on_press) as listener:
    listener.join()

f.close()
quit()