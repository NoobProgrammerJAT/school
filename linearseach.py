import random

array = [random.randint(1,100) for i in range (10)]
print (array)
x = int(input("Enter a number to find: "))
count = 0 
found = False
while count <= len(array) and found == False:
    if x == array[count]:
        print("Number is found at index", count)
        found = True 
    else:
        count = count + 1
if found == False:
    print ("Item not found")