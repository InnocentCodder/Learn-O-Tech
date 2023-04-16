import csv

print()
print()
print("------------------------------------------------")
print("Welcome to Spell-Bee ....Bee The next champion! :)")
print("------------------------------------------------")
print()
print("********Enter 5 anytime to quit the Quiz********\n")
with open("spell.csv", 'r') as f:
    csvreader = csv.reader(f, delimiter=',')
    score = 0

    print("your score is", 0, "\n")
    for i in csvreader:
        print("================================================\n")
        print("***Select option for correct spelling***\n")
        print(i[0], i[1], i[2], i[3], "\n")

        print("Enter correct option")
        print("1  ", "2  ", "3  ", "4\n")
        choice = int(input())
        print()
        if choice == 5:
            break
        if choice == int(i[4]):

            print("congratulations.......Correct Answer!\n")
            score = score+1
            print(f"     ----------Your Score is: {score}----------\n")
        else:
            print("Sorry... incorrect answer! :(\n")
            print(f"The correct answer is: {i[int(i[4])-1]}\n")
            print(f"     ----------Your Score is: {score}----------\n")

        continue

print("================================================")
print("       Thankyou for playing this game.")
print("================================================")
print()
print()
print()
print()
