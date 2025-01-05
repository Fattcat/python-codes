import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import pyautogui

# Vytvorenie screenshotu
screenshot = pyautogui.screenshot()

# Inverzia farieb obrázka
inverted_screenshot = ImageOps.invert(screenshot.convert('RGB'))

# Inicializácia počítadla pre zobrazenie obrázkov
count = 0

# Funkcia na zobrazenie normálneho alebo inverzného obrázka
def display_image():
    global count

    # Určenie, ktorý obrázok sa má zobraziť (pôvodný alebo inverzný)
    if count % 2 == 0:
        tk_screenshot = ImageTk.PhotoImage(screenshot)
    else:
        tk_screenshot = ImageTk.PhotoImage(inverted_screenshot)

    # Aktualizovanie obrázka v Tkinter okne
    label.config(image=tk_screenshot)
    label.image = tk_screenshot

    # Zvýšenie počítadla
    count += 1

    # Po 8 zobrazeniach (4 normálne a 4 inverzné) ukončiť program
    if count < 9:
        root.after(300, display_image)
    else:
        root.quit()

# Vytvorenie hlavného okna Tkinter
root = tk.Tk()
root.title("Alternating Screenshot")
root.attributes("-fullscreen", True)
root.config(bg="black")

# Zobrazenie pôvodného obrázka v okne
label = tk.Label(root)
label.pack()

# Zavolanie funkcie na striedanie obrázkov
display_image()

# Spustenie hlavnej slučky Tkinter
root.mainloop()
