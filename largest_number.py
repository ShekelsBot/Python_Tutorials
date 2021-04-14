#Largest Number 2.0
#test_1 = 5
#test_2 = 10
#test_3 = 37




def test_averager(test_1,test_2,test_3):
    global max
    if (test_1 >= test_2) and (test_1 >= test_3):
        max = test_1
    elif (test_2 >= test_1) and (test_2 >= test_3):
        max = test_2
    else:
        max = test_3
    avg = test_1 + test_2 + test_3
    print ("Average is:",avg)
    print ("Highest Score is:",max)
test_averager(5,10,37)
