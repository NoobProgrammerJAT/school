#Binary search
#Used when you are dealing with a sorted array already 
#mid value = [INT(low + high)/2]

array = [12,13,43,66,77,99,100,234]


last = len(array) - 1
low = 0
high = len(array)-1
mid = int((low +last)/2)
found = False

search = int(input("Enter a value to search: "))
while found == False:

    if search == array[mid]:
        print ("The number is found on index", mid)
        found = True 
    elif search > array[mid]:
        low = mid + 1
        mid =int((low + high)/2)
    else:
        high = mid - 1
        mid = int((low+ high)/2)
