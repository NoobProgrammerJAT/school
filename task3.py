import random 

array =[[random.randint(1,50) for i in range (5)], [random.randint(1,20) for i in range(5)], [random.randint(1,30) for i in range (5)], [random.randint(1,35) for i in range (5)]]

print (array)
search = int(input("Enter a number to find: "))

col = len(array[0])
row = len(array)
found = False

for x in range (row):
    for y in range (col):
        if search == array[x][y]:
            found = True
        
if found:
    print ("Item is found on column ", x," and on row ",y)
else:
    print ("Item not found")



