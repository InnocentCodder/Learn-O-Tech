import pygame
from pygame.locals import *
from pygame import mixer
from sty import Style, RgbFg, fg, bg, ef, rs
#Custom Colors start

fg.saffron = Style(RgbFg(255, 144, 5))
from colorama import Fore, init
#Custom Color End

init(autoreset=True)

pygame.init()

mixer.init()
mixer.music.load('summer.mp3')
mixer.music.set_volume(0.7)
mixer.music.play(50)

while True:
    print("--------------------------------------------------")
    print(Fore.RED + "             Welcome to Lern-O-Tech")
    print("--------------------------------------------------")
    print(Fore.BLUE + "PRESS: ")
    print(fg.saffron + "1. For Spell-Bee challenge" + fg.rs)
    print(fg.saffron + "2. For What's My Full Form" + fg.rs)
    print('3. For General Knowledge')
    print('4. For Maths-Magic')
    print(Fore.GREEN + "5. For Basic Science Formulas")
    print(Fore.GREEN + "6. To play/pause music\n\n")
    print(Fore.RED + "********Enter 0 to quit the Quiz********\n")
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
print(Fore.BLUE + "       Thankyou for playing this Quiz.")
print("================================================")
print()
print()
print()
print()
