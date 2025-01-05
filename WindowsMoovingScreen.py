import pygame
import threading
import time
import pygetwindow as gw

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("bruh.mp3")
    pygame.mixer.music.play(-1)  # -1 znamená nekonečné opakovanie

def move_all_windows():
    try:
        windows = gw.getAllWindows()
        print(f"Nájdených {len(windows)} otvorených okien.")
        
        if not windows:
            print("Neboli nájdené žiadne otvorené okná.")
            return

        while True:
            for window in windows:
                if window.title:  # Preskočiť okná bez názvu
                    try:
                        print(f"Pohyb okna: {window.title}")
                        # Posun o 40 pixelov vľavo
                        window.moveTo(window.left - 40, window.top)
                        time.sleep(0.01)  # Rýchlejší pohyb (10 ms)
                        # Posun o 40 pixelov vpravo
                        window.moveTo(window.left + 40, window.top)
                        time.sleep(0.01)  # Rýchlejší pohyb (10 ms)
                    except Exception as e:
                        print(f"Chyba pri pohybe okna '{window.title}': {e}")
    except Exception as e:
        print(f"Chyba: {e}")

# Spusti prehrávanie piesne v samostatnom vlákne
song_thread = threading.Thread(target=play_song)
song_thread.start()

# Spusti pohyb všetkých okien
move_all_windows()
