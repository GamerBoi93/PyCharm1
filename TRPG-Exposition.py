import time


def exposition():
    print("")


#Start Of Intro Scene
print("Hello Young Adventurer, What Is Your Name?")
print("")
Name = (input(""))
print("")
print("Well Hello There", Name, "")
print("")
print("Lets Get You Started Off By Choosing You A Class!")
print("")
time.sleep(0.5)
print("Would You Like To Be Fast Like A Rogue?")
print("")
time.sleep(1)
print("Or Maybe Unpredictable Like A Mage?")
print("")
time.sleep(1)
print("Or A Well Rounded Fighter Like A Knight?")
print("")
time.sleep(1)
print("Make Sure To Put Some Thought Into Your Choice,")
time.sleep(0.5)
print("Once Chosen You Wont Be Able To Switch!")
print("")
time.sleep(1)
# End Of Intro Scene

# Start Of Class Selection
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
        if yn1 == "yes":
            x = 1

        elif yn1 == "Yes":
            x = 1

    elif Class == 2:
        print("You Would Like To Be A Rogue?")
        yn1 = input("")
        print("")
        if yn1 == "yes":
            x = 1

        elif yn1 == "Yes":
            x = 1

    elif Class == 3:
        print("You Would Like To Be A Mage?")
        yn1 = input("")
        print("")
        if yn1 == "yes":
            x = 1

        elif yn1 == "Yes":
            x = 1

    else:
        print("")

# End Of Class Selection

# Start Of Exposition
time.sleep(2)
print("You Wake Up On The Ground In A Dimly Lit Colosseum.")
print("")
time.sleep(1)
print('"Welcome To The Arena!" The Shop Merchant Behind You Said.')
print("")
time.sleep(1)
print('"Well, No Time For Talking, Lets Get To Fighting!"')
