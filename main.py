while True:
    print("--------------------------------------------------")
    print("             Welcome to Lern-O-Tech")
    print("--------------------------------------------------")
    print('''Press:
    1. For Spell-Bee challenge
    2. For What's My Full Form
    3. For General Knowledge
    4. For Maths-Magic
    5. For Basic Science Formulas

    ***Enter 0 to Quit the Lern-O-Tech***''')

    choice = 0

    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        import spell
    if choice ==2:
        import abbreviation
    if choice==3:
        import gk
    if choice==4:
        import mm
    if choice == 5:
        import formula
    if choice == 0:
        break
print()
print()
print("================================================")
print("       Thankyou for playing this Quiz.")
print("================================================")
print()
print()
print()
print()
