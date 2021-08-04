from pynput import keyboard
import os

def on_activate():
    os.system("python3 /Users/lichunlin/Desktop/Focus.AI/Demo_Edward/DemoOnly.py")

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<cmd>+;'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()
