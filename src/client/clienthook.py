import requests
import time
import threading
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image, ImageSequence
from random import randint
import json

SERVER_URL = 'http://localhost/python/clientHook/trigger?get_status=clicked'

def check_for_signal():
    while True:
        try:
            response = requests.post(SERVER_URL)
            data = response.json()
            if response.status_code == 200:
                if(data['message'] == 'user clicks'):
                    # NOW DO SOME MYSQL QUERY HERE OR IN REQUEST
                    show_popup()
                else:
                    print(data['message'])
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(5) 

def show_popup():
    root = tk.Tk()
    root.overrideredirect(True)
    root.title("ALERT!")
    
    def move_window():
        root.geometry(f"950x500+{randint(10, 100)}+{randint(10, 100)}")
        root.after(10, move_window)
    
    image_pic = Image.open("C:\\wamp64\\www\\python\\clientHook\\dist\\hack.gif")
    frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(image_pic)]
    label = tk.Label(root)
    label.pack(padx=0, pady=0, fill='both', expand=True)

    def animate(index):
        frame = frames[index]
        label.configure(image=frame)
        root.after(100, animate, (index + 1) % len(frames))
    
    root.after(0, animate, 0)
    text_label = tk.Label(root, text="YOU HAVE BEEN HACKED! YOUR FILES WILL BE ENCRYPT FOREVER OR GIVE ME 10 BITCOIN!", font=("Helvetica", 15))
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
