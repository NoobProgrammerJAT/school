import random
myarray = [random.randint(1,100) for i in range (10)]
print (myarray)
sum = 0
for x in range (9):
    sum = myarray[x] + sum
    if myarray [x] > myarray [x+1]:
        max = myarray [x]
    elif myarray [x] < myarray [x+1]:
        min = myarray [x]

print (sum)
print (max)
print (min)