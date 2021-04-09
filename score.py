holder = 1
array = []
for i in range (0, 5):
    array.append(int(input("Enter score: ")))
    holder = holder + 1

avg = sum(array)/len(array)
#print(array)
print ("Average score:",avg)