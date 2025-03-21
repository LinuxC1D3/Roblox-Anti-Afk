import random
import keyboard
import time
import pygetwindow as gw
import ctypes

SendInput = ctypes.windll.user32.SendInput

# Virtuelle Tastencodes für Roblox-Steuerung
key_map = {
    'w': 'w',
    'a': 'a',
    's': 's',
    'd': 'd',
    'space': 'space'
}

def get_interval(interval):
    return random.randint(60, 600) if interval is None else interval

def action(keys):
    random.shuffle(keys)
    for key in keys:
        keyboard.press(key)  # Tastendruck simulieren
        time.sleep(random.uniform(0.1, 3))  # Zufällige Haltezeit
        keyboard.release(key)  # Taste loslassen

def get_roblox_window():
    # Suche nach Fenstern mit dem Titel "Roblox"
    windows = gw.getWindowsWithTitle("Roblox")
    if not windows:
        return None

    for window in windows:
        print(f"Fenster Titel: {window.title}, Handle: {window._hWnd}")  # Debug: Zeigt Fenstertitel und Handle an
        if "Roblox" in window.title:  # Suche nach 'Roblox' im Titel
            return window
    return None

def bring_to_foreground(window):
    # Versuche, das Fenster ins Vordergrund zu bringen
    try:
        if window.isMinimized:  # Wenn das Fenster minimiert ist, versuche es wiederherzustellen
            window.restore()
        window.activate()
        time.sleep(0.5)  # Kurze Pause, um sicherzustellen, dass das Fenster aktiviert wurde
    except Exception as e:
        print(f"Fehler beim Aktivieren des Fensters: {e}")

def main():
    interval_choice = input('[1] Random intervals\n[2] Fixed interval\n>>> ')
    mode_choice = input('[1] All keys\n[2] Movement keys\n[3] Jump Key\n>>> ')

    interval = None if interval_choice == '1' else int(input('Enter interval in seconds: '))

    keys = {
        '1': ['space', 'w', 'a', 's', 'd'],
        '2': ['w', 'a', 's', 'd'],
        '3': ['space']
    }.get(mode_choice, ['space'])

    return interval, keys

if __name__ == '__main__':
    print(r"""
    Created by
  _       _________ _                            _______  __    ______   ______  
 ( \      \__   __/( (    /||\     /||\     /|  (  ____ \/  \  (  __  \ / ___  \ 
 | (         ) (   |  \  ( || )   ( |( \   / )  | (    \/\/) ) | (  \  )\/   \  \
 | |         | |   |   \ | || |   | | \ (_) /   | |        | | | |   ) |   ___) /
 | |         | |   | (\ \) || |   | |  ) _ (    | |        | | | |   | |  (___ ( 
 | |         | |   | | \   || |   | | / ( ) \   | |        | | | |   ) |      ) \
 | (____/\___) (___| )  \  || (___) |( /   \ )  | (____/\__) (_| (__/  )/\___/  /
 (_______/\_______/|/    )_)(_______)|/     \|  (_______/\____/(______/ \______/ 
""")

    interval, keys = main()

    while True:
        roblox_window = get_roblox_window()
        if roblox_window:
            bring_to_foreground(roblox_window)  # Versuche, das Fenster ins Vordergrund zu bringen
            action(keys)  # Tasten senden
        else:
            print("Roblox nicht gefunden. Warte...")

        time.sleep(get_interval(interval))  # Pause zwischen den Aktionen