import random
#from TRPG-Exposition.py import *

def firstfight():

    mlvl = 1
    monster = "Slime"
    items = 0

    print("")
    print("A LVL", mlvl, monster, "Has Appeared!")
    print("")
    print("What Will You Do?")

    fighting = True

    while fighting:
        print("1. Fight     2. Item     3. Run")
        fight1 = int(input(""))

        if fight1 == 1:
            print("")

        elif fight1 == 2:
            if items == 0:
                print("You Have No Items!")

        elif fight1 == 3:
            print("The Merchant Wont Let You Leave!")
