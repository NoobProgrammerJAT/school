 #LinkedListData = [5, 6, 7, 9, None, None, None]
 #LinkedListPointer = [-1, 0, 1, 2, 5, 6, -1]
StartPointer = 3
HeapPointer = 4
ItemPointer = 3
LinkedListData = [5, 6, 7, 9, None, None, None]
LinkedListPointer = [-1, 0, 1, 2, 5, 6, -1]
Size = 7
#while StartPointer != -1:
    #print (LinkedListData[StartPointer])
    #StartPointer = LinkedListPointer[StartPointer]

#Searching element in the linked list

def search_ll(item):
    global ItemPointer, PreviousPointer
    while ItemPointer != -1:
        if item == LinkedListData[ItemPointer]:
            return ItemPointer
        else: 
            PreviousPointer = ItemPointer
            ItemPointer = LinkedListPointer[ItemPointer]
            
    return -1   

# print(search_ll (search))

#Adding into a linked list
def add_ll(addition):
    global StartPointer, HeapPointer
    if HeapPointer != -1:
        TempPointer = StartPointer
        StartPointer = HeapPointer
        LinkedListData[StartPointer] = addition
        HeapPointer = LinkedListPointer[HeapPointer]
        LinkedListPointer[StartPointer] = TempPointer
    else:
        return -1 



#Deleting from linked list
def delete_ll(item):
    global StartPointer, HeapPointer
    if StartPointer != -1: 
        if search_ll(item) != -1:
            LinkedListData[ItemPointer] = None
            TemporaryPointer = LinkedListPointer[ItemPointer]
            LinkedListPointer[ItemPointer] = HeapPointer
            LinkedListPointer[PreviousPointer] = TemporaryPointer
            HeapPointer = ItemPointer
        else:
            return -1
    else:
        return -1
    
item = int(input("Enter item to delete: "))
delete_ll(item)
print(LinkedListData)
print(LinkedListPointer)
addition = int(input("Enter the element to add: "))
add_ll(addition)
print(LinkedListData)
print(LinkedListPointer)
item2 = int(input("Add second number: "))
add_ll(item2)
print(LinkedListData)
print(LinkedListPointer)