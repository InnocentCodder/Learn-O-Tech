import csv

print()
print()
print("------------------------------------------------")
print("Welcome to Full-Form ....Can you score full marks! :)")
print("------------------------------------------------")
print()
print("********Enter 5 anytime to quit the Quiz********\n")
with open("abbreviation.csv", 'r') as f:
    csvreader = csv.reader(f, delimiter=',')
    score = 0

    print("your score is", 0, "\n")
    for i in csvreader:
        print("================================================\n")
        print("***Select option for correct spelling***\n")
        print(f"What is the full form of {i[0]}")
        print(f"1.{i[1]}\n2.{i[2]}\n3.{i[3]}\n4.{i[4]}\n")

        print("Enter correct option")
        print("1  ", "2  ", "3  ", "4\n")
        choice = int(input()) + 1
        print()
        if choice == 6:
            break
        if choice == int(i[5]):

            print("congratulations.......Correct Answer!\n")
            score = score + 1
            print(f"     ----------Your Score is: {score}----------\n")
        else:
            print("Sorry... incorrect answer! :(\n")
            print(f"The correct answer is: {i[int(i[5])-1]}\n")
            print(f"     ----------Your Score is: {score}----------\n")

        continue

print("================================================")
print("       Thankyou for playing this game.")
print("================================================")
print()
print()
print()
print()