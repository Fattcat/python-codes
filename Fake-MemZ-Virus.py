import pyautogui
import time
from tkinter import Tk, Label
from PIL import Image, ImageTk

def show_image(image):
    # Vytvoriť tkinter okno na zobrazenie obrázka
    root = Tk()
    root.title("Screenshot")
    root.attributes("-fullscreen", True)
    root.config(bg="black")
    
    # Prevod obrázka na formát kompatibilný s Tkinter
    photo = ImageTk.PhotoImage(image)

    # Zobraziť obrázok v okne
    label = Label(root, image=photo)
    label.pack()

    # Ukážeme okno a čakáme, kým sa nezatvorí
    root.update()
    return root, label

def process_screenshot():
    # Urobíme screenshot celej obrazovky
    screenshot = pyautogui.screenshot()

    # Začíname so šírkou a výškou obrázku
    width, height = screenshot.size

    while width > 200 and height > 150:
        # Zobrazenie obrázku na obrazovke
        root, label = show_image(screenshot)

        # Čakáme 0.6 sekundy pred zmenšením obrázka
        time.sleep(0.1)

        # Zmenšujeme obrázok o 30px na každej strane
        width -= 50
        height -= 30
        screenshot = screenshot.crop((15, 15, width + 15, height + 15))

        # Uzavrieme staré okno a zobraziť nový obrázok
        root.destroy()

        # Vytvoríme nový obrázok
        screenshot = screenshot.resize((width, height))

# Spustíme funkciu
process_screenshot()
