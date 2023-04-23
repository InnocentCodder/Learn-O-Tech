def main():
    import csv

    from colorama import Fore, init

    init(autoreset=True)

    print()
    print()
    print("------------------------------------------------")
    print(Fore.BLUE + "Welcome to GK ....Kaun Banega Crorepati :)")
    print("------------------------------------------------")
    print()
    print(Fore.LIGHTRED_EX +
          "********Enter 5 anytime to quit the Quiz********\n")
    with open("gk.csv", 'r') as f:
        csvreader = csv.reader(f, delimiter='!')
        score = 0

        print("your score is", 0, "\n")
        for i in csvreader:
            print("================================================\n")
            print(Fore.GREEN + "***Select option for correct option***\n")
            print(Fore.RED + f"{i[0]}")
            print(Fore.LIGHTYELLOW_EX +
                  f"1.{i[1]}\n2.{i[2]}\n3.{i[3]}\n4.{i[4]}\n ")

            print("Enter correct option")
            print("1  ", "2  ", "3  ", "4\n")
            choice = int(input()) + 1
            print()
            if choice == 6:
                break
            if choice == int(i[5]):

                print(Fore.GREEN + "congratulations.......Correct Answer!\n")
                score = score + 1
                print(f"     ----------Your Score is: {score}----------\n")
                print(Fore.GREEN + f"{i[6]}")
            else:
                print(Fore.RED + "Sorry... incorrect answer! :(\n")
                print(Fore.GREEN +
                      f"The correct answer is: {i[int(i[5])-1]}\n")
                print(f"     ----------Your Score is: {score}----------\n")
                print(Fore.GREEN + f"{i[6]}")

            continue

    print("================================================")
    print(Fore.BLUE + "       Thankyou for playing this game.")
    print("================================================")
    print()
    print()
    print()
    print()


if __name__ == "__main__":
    main()