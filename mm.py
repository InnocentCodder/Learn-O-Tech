import random as rand

from colorama import Fore, init

init(autoreset=True)

print()
print()
print("------------------------------------------------")
print(Fore.BLUE + "Welcome to Math-Magic ...Feel the magic of math:)")
print("------------------------------------------------")
print()
print(Fore.RED + "********Enter 0 anytime to quit the Quiz********\n")
count = 1
score = 0
print(f"     ----------Your Score is: {score}----------\n")
print("================================================\n")
while count < 11:
    i = rand.randrange(2, 21)
    j = rand.randrange(1, 11)
    count += 1
    print(Fore.RED + f"{i} * {j}")
    user_input = int(input("Enter the correct answer = "))
    if user_input == i * j:
        score += 1
        print(Fore.GREEN + "congratulations.......Correct Answer!\n")
        print(f"     ----------Your Score is: {score}----------\n")
        print("================================================")
    elif user_input == 0:
        print()
        print()
        break
    else:
        print(Fore.RED + "Sorry... incorrect answer! :(\n")
        print(Fore.GREEN + "Correct answer is:", i * j, "\n")
        print(f"     ----------Your Score is: {score}----------\n")

print("================================================")
print(Fore.BLUE + "       Thankyou for playing this game.")
print("================================================")
print()
print()
print()
print()