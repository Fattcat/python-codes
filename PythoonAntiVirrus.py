import os
import psutil
import time

# Definovanie priečinkov, ktoré chceme skenovať
FOLDER_PATHS = [
    os.path.expanduser("~\\Downloads"),  # Downloads
    os.path.expanduser("~\\Desktop"),    # Desktop
    "C:\\Windows\\System32",             # System32
    os.path.expanduser("~\\AppData"),    # APPDATA
    os.path.expanduser("~\\Documents"),  # Documents
    os.path.join(os.path.expanduser("~"), "AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")  # Startup
]

def get_running_python_processes():
    """Získa zoznam spustených Python procesov a ich argumentov."""
    running_files = set()
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] and 'python' in proc.info['name'].lower():
                cmdline = proc.info['cmdline']
                if cmdline:
                    for arg in cmdline[1:]:
                        # Skontroluje, či sa argumenty nachádzajú v určených priečinkoch
                        for folder in FOLDER_PATHS:
                            if arg.startswith(folder) and (arg.endswith(".py") or arg.endswith(".pyw")):
                                running_files.add(os.path.abspath(arg))
                    # Skrytý proces - kontrola 'pythonw'
                    if 'pythonw' in proc.info['name'].lower():
                        for arg in cmdline[1:]:
                            for folder in FOLDER_PATHS:
                                if arg.startswith(folder) and (arg.endswith(".py") or arg.endswith(".pyw")):
                                    running_files.add(os.path.abspath(arg))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return running_files

def monitor_running_scripts():
    """Nepretržite monitoruje spustené Python skripty v špecifikovaných priečinkoch."""
    seen_files = set()
    while True:
        running_files = get_running_python_processes()
        new_files = running_files - seen_files
        
        for file in new_files:
            print("---------- AntyVirrus ----------")
            print(f"Súbor: {os.path.basename(file)}")
            print(f"Cesta: {file}")
            print("-" * 40)
        
        seen_files = running_files
        time.sleep(1)  # Kontrola každú sekundu

if __name__ == "__main__":
    monitor_running_scripts()