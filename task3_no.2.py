import random 

array =[[random.randint(1,50) for i in range (5)], [random.randint(1,20) for i in range(5)], [random.randint(1,30) for i in range (5)], [random.randint(1,35) for i in range (5)]]

print (array)
search = int(input("Enter a number to find: "))


col = len(array[0])
row = len(array)
found = False
r = int(input("Enter the row no. to find: "))

for x in range (col):
    if search == array [r-1][x]:
        found = True 
        print ("The value is found in column", x + 1)

if not found:
    print ("Item is not found")
