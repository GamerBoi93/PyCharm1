import random
for x in range(1):
  print( random.randint(1,101) )

# Class Selection Screen
x = 0

while x == 0:
    print("What Class Would You Like To Chose?")
    print("1. Knight    2. Rogue    3. Mage")
    print("")
    Class = int(input(""))
    print("")

    if Class == 1:
        print("You Would Like To Be A Knight?")
        yn1 = input("")
        print("")
        if yn1 == ("yes"):
            x = 1

    elif Class == 2:
        print("You Would Like To Be A Rogue?")
        yn1 = input ("")
        print("")
        if yn1 == ("yes"):
            x = 1

    elif Class == 3:
        print("You Would Like To Be A Mage?")
        yn1 = input ("")
        print("")
        if yn1 == ("yes"):
            x = 1

    else:
        print ("What?")
