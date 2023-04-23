import csv

from colorama import Fore, init

init(autoreset=True)

print()
print()
print("------------------------------------------------")
print(Fore.BLUE + "Welcome to Spell-Bee... Bee The next champion! :)")
print("------------------------------------------------")
print()
print(Fore.RED + "********Enter 6 anytime to quit the Quiz********\n")
with open("spell.csv", 'r') as f:
    csvreader = csv.reader(f, delimiter='!')
    score = 0

    print("your score is", 0, "\n")
    for i in csvreader:
        print("================================================\n")
        print(Fore.GREEN + "***Select option for correct spelling***\n")
        print(Fore.RED + f"{i[0]} {i[1]} {i[2]} {i[3]} \n")

        print(Fore.LIGHTYELLOW_EX + "Enter correct option")
        print("1  ", "2  ", "3  ", "4\n")
        choice = int(input())
        print()
        if choice == 6:
            break
        if choice == int(i[4]):

            print(Fore.GREEN + "congratulations.......Correct Answer!\n")
            score = score + 1
            print(f"     ----------Your Score is: {score}----------\n")
            print(f"The meaning of {i[int(i[4])-1]} is: {i[5]}")
        else:
            print(Fore.RED + "Sorry... incorrect answer! :(\n")
            print(Fore.LIGHTGREEN_EX +
                  f"The correct answer is: {i[int(i[4])-1]}\n")
            print(f"     ----------Your Score is: {score}----------\n")
            print(f"The meaning of {i[int(i[4])-1]} is: {i[5]}")

        continue

print("================================================")
print(Fore.BLUE + "       Thankyou for playing this game.")
print("================================================")
print()
print()
print()
print()
