#Andrew Bruckbauer
#4/4/2021
#Blast off

def blast_off():
    counter = 10
    while counter >= 0:
        if counter > 0:
            print (counter)
            counter = counter - 1
        else:
            print ("Blast off")
            break

blast_off()