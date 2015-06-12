__author__ = 'Hannie'


import random
x = 1
cont = True
while cont:
    ok = input("Next turn? (y/n) ")
    print()
    if ok == "y":
        COLOURS = ("Red", "Yellow", "Green", "Blue")
        print("TURN {}: {} {}".format(x, random.choice(COLOURS), random.randint(1, 4)))
        print()
        x += 1
    elif ok == "n":
        print("Jenga fell at TURN {}.".format(x-1))
        print("Thank you for playing!")
        cont = False
    else:
        print("Invalid choice entered. Please try again.")
        print()
