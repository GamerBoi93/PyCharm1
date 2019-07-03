import time


def exposition():
    print("")


# Start Of Intro Scene
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
            Class = "Knight"
        elif yn1 == "Yes":
            x = 1
            Class = "Knight"
    elif Class == 2:
        print("You Would Like To Be A Rogue?")
        yn1 = input("")
        print("")
        if yn1 == "yes":
            x = 1
            Class = "Rogue"
        elif yn1 == "Yes":
            x = 1
            Class = "Rogue"
    elif Class == 3:
        print("You Would Like To Be A Mage?")
        yn1 = input("")
        print("")
        if yn1 == "yes":
            x = 1
            Class = "Mage"
        elif yn1 == "Yes":
            x = 1
            Class = "Mage"
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


import random

# Player Stats

level = 1
xppoints = 0
items = 0
attack = 1
defense = 1
speed = 1
luck = 1
magic = 1
health = 25

if Class == "Mage":
    attack = 3
    defense = 4
    speed = 2
    luck = 4
    magic = 7
elif Class == "Rogue":
    attack = 5
    defense = 2
    speed = 5
    luck = 6
    magic = 2
elif Class == "Knight":
    attack = 4
    defense = 4
    speed = 4
    luck = 4
    magic = 4

# End Of Player Stats

# Monster Stats

monster = "Slime"
mattack = 1
mdefense = 1
mspeed = 2
mlvl = int(1)
mluck = int(1)
mhealth = int(10)

# End Of Monster Stats

print("")
print("A LVL", mlvl, monster, "Has Appeared!")
print("")
print("What Will You Do?")

fighting = True

while fighting:

    print("1. Fight     2. Item     3. Run")
    mspeed = ((mspeed * (mluck / 2)) / 2) - random.randint(1, 6)
    speed = ((speed * (luck / 2)) / 2) - random.randint(1, 6)
    fight1 = int(input(""))

    # if fight1 == 1:
    if speed > mspeed:
        damage = ((attack * 5)(luck / 4) / 2) / mdefense
        round(int(damage))
        print (damage)
        print("You Attacked The Slime And Delt", damage, "Damage!")
        mhealth - damage
        if mhealth <= 0:
            print("The Slime Had Been Defeated!")
            xppoints = mlvl * 5
            if xppoints > (level^2 + 10) *3:
                xppoints - (level^2 + 10) *3
                level + 1
                attack + 1
                defense + 1
                speed + 1
                magic + 1
                health + 2

        elif mhealth > 0:
            print ("")
            print("The Slime Now Has", mhealth,  "Health Remaining!")

    elif mspeed > speed:
        mattack = mattack
        mdamage = ((mattack * 5)(mluck / 4) / 2) / defense

        print("You Attacked The Slime And Delt", damage, "Damage!")
        health - mdamage
        if health <= 0:
            print("You Have Been Defeated!")

        elif mhealth > 0:
            print("")
            print("You Now Have", health, "Health Remaining!")

    elif fight1 == 2:
        if items == 0:
            print("You Have No Items!")

    elif fight1 == 3:
        print("The Merchant Wont Let You Leave!")
