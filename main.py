import pygame
from pygame.locals import *
from pygame import mixer

from colorama import Fore, init

init(autoreset=True)

pygame.init()

mixer.init()
mixer.music.load('summer.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("--------------------------------------------------")
    print(Fore.RED + "             Welcome to Lern-O-Tech")
    print("--------------------------------------------------")
    print(Fore.BLUE+'''Press:
    1. For Spell-Bee challenge
    2. For What's My Full Form
    3. For General Knowledge
    4. For Maths-Magic
    5. For Basic Science Formulas
    6. To play/pause music

    ***Enter 0 to Quit the Lern-O-Tech***''')

    choice = 0

    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        import spell
    if choice == 2:
        import abbreviation
    if choice == 3:
        import gk
    if choice == 4:
        import mm
    if choice == 5:
        import formula
    if choice == 0:
        break
    if choice == 6:
        if mixer.music.get_busy() == True:
            mixer.music.pause()
            continue
        if mixer.music.get_busy() == False:
            mixer.music.unpause()

print()
print()
print("================================================")
print("       Thankyou for playing this Quiz.")
print("================================================")
print()
print()
print()
print()
