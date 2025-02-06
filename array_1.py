myArr1= []

#Array by default is not supported byt python. It only supports lists

#How to initialize array in python
#Example : array of size 10

#For integer
myArr2= [0] * 10
myArr3 = [0,0,0,0,0,0,0,0,0,0]

#Alternative Method 

myArr = [0 for i in range(10)]
print (myArr)

#For string - cambridge requires to use double quotes
myArr4= [""] * 10
#to print output of the array 
for i in range (0,len(myArr4)):
    print (myArr4[i])

#Best possible way to initialize array 
myArr_ = [None for i in range (10)]

#Suitable for paper 4 to print an array as a seperate question
for element in myArr_:
    print (element)

#To store and print random data in array 
import random 
myArray = [random.randint(1,100) for i in range (10)]
print (myArray)

#Creating 2D Arrays 
myarray = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]
print (myarray)

#For printing a 2D Array 
for row in range (4):
    for col in range (4):
        print (myarray[row][col], end = "")
    print ()