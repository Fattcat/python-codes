import ctypes
import time
import random

def create_popup():
    messages = [
        "Memz virus is watching you!",
        "Your system is going down...",
        "Why did you run this program?",
        "Error 404: Sanity not found"
    ]
    for i in range(3):
        ctypes.windll.user32.MessageBoxW(0, random.choice(messages), "Warning", 1)
        time.sleep(0.5)

create_popup()
