import random
min = 1
max = 6
bank = 11
high = 0
roll_again = "yes"

while roll_again == "yes" or roll_again == "y" and bank != 0:
    dice1 = (random.randint(min, max))
    dice2 = (random.randint(min, max))
    print ("Rolling the dices...")
    print ("The values are....")
    print ("dice 1 = ",dice1)
    print ("dice 2 = ",dice2)
    total = dice1 + dice2
    print ("Roll Total ",total )
    if dice1 + dice2 == 7:
        bank = bank + 4
        if bank > high:
            high = bank
        else:
            break
    elif bank == 0:
        print ("You're broke! You had $",high," before loosing it all!")
    else:
        bank = bank - 1

    print ("You have a balance of:" ,bank)
    print ("You're current high is: ",high)
    roll_again = input("Roll the dices again? ")
