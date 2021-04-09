import random
min=1
max=6
bank=2
high=10

roll_again = str(input("Would you like to roll? "))
roll_count = 0

while roll_again == "yes" or roll_again == "y" and bank != 0:

    dice1 = (random.randint(min, max))
    dice2 = (random.randint(min, max))

    print ("dice 1 = ",dice1)
    print ("dice 2 = ",dice2)

    total = dice1 + dice2
    roll_count = roll_count + 1
    print ("Roll Total ",total )

    if total == 7:
        bank = bank + 4
        print ("You have a balance of:" ,bank)
        if bank > high:
            high = bank
            print ("You're current high is: ",high)
        else:
            exit
    elif total != 7:
        bank = bank -1
        print ("Bad role current balance: ",bank)
        print ("You're current high is: ",high)
        if bank == 0:
            print ("You're broke! You had ",high,"Dollars before loosing it all after",roll_count, "rolls!")
            break
        else:
            exit
    else:
        print("error")

    roll_again = input("Roll the dices again? ")