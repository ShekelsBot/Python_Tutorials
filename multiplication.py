print ("This program will solve multiplication problems.")
print ("Enter 0 for both terms to quit.")

first = int(input("First number: "))
second = int(input("Second number: "))
while first != 0 and second != 0:

    third = first * second

    print (first, " x " ,second, " = " ,third,)

    first = int(input("First number: "))
    second = int(input("Second number: "))

if first == 0 and second == 0:
    print ("Goodbye!")
