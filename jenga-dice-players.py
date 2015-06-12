__author__ = 'Hannie'

# to spice up the game, specify which players will play each turn!

import random
cont = True
while cont:
    ok = input("Next turn? (y/n) ")
    print()
    if ok == "y":
        COLOURS = ("Red", "Yellow", "Green", "Blue")
        # insert names of players
        PLAYERS = ("Name1", "Name2", "Name3")
        print("{}: {} {}".format(random.choice(PLAYERS), random.choice(COLOURS), random.randint(1, 4)))
        print()
    elif ok == "n":
        print("Jenga fell. :-(")
        print("Thank you for playing!")
        cont = False
    else:
        print("Invalid choice entered. Please try again.")
        cont = False
