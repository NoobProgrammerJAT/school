import random 

array =[[random.randint(1,50) for i in range (5)], [random.randint(1,20) for i in range(5)], [random.randint(1,30) for i in range (5)], [random.randint(1,35) for i in range (5)]]

swap = True 
row = len(array)
col = len(array[0])

for x in range (row):
    top = len(array[0]) - 1
    swap = True
    while swap and top != 0:
        for y in range (col -1):
            if array [x][y - 1]:
                