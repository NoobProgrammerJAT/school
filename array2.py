#Task 2 
#Find total of all elements of each row
#Find the total of the elements for each column
#Find the highest in each row
#Find the highest in each column

array = [[1,2,3,4], [10,14,154,17],[32,44,55,66],[78,90,10,200]]
sum1 = 0
sum2 = 0
maxrow = array[0]
maxcol = array [1]
for x in range (len(array[0])-1):
    sum1 = sum1 + maxrow [x]
    if array [x] > array [x+1]:
        max_row = array [x]
    for y in range (len(array[1])-1):
        print (array [x][y], end = "")
        print ()
        sum2 = sum2 + maxcol [y]
        if array [y] > array [y+1]:
            max_column = array [y]

        
print (sum1)
print (sum2)
print (max_row)
print (max_column)