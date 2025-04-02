import os

# Definovanie priečinkov, ktoré chceme skenovať
FOLDER_PATHS = [
    os.path.expanduser("~\\Desktop"),    # Desktop
    os.path.expanduser("~\\AppData\Roaming"),  # APPDATA
    os.path.expanduser("~\\Documents"),  # Documents
    os.path.expanduser("~\\Downloads"),  # Downloads
    "C:\\Windows\\System32"              # System32
]

def find_python_files():
    """Prehľadá priečinky a nájde .py a .pyw súbory."""
    found_files = []
    
    # Pre každý priečinok
    for folder in FOLDER_PATHS:
        if os.path.exists(folder):  # Skontrolujeme, či priečinok existuje
            for root, dirs, files in os.walk(folder):  # Prechádzame všetky podpriečinky
                for file in files:
                    if file.endswith(".py") or file.endswith(".pyw"):
                        file_path = os.path.join(root, file)
                        found_files.append(file_path)  # Pridáme nájdený súbor do zoznamu
                        
    return found_files

def main():
    """Spustí hľadanie Python súborov a vypíše výsledky."""
    python_files = find_python_files()
    
    if python_files:
        print("Nájdené Python súbory:")
        for file in python_files:
            print(f"Súbor: {os.path.basename(file)}")
            print(f"Cesta: {file}")
            print("-" * 40)
    else:
        print("Neboli nájdené žiadne .py alebo .pyw súbory.")

if __name__ == "__main__":
    main()
