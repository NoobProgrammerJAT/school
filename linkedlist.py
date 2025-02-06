 #LinkedListData = [5, 6, 7, 9, None, None, None]
 #LinkedListPointer = [-1, 0, 1, 2, 5, 6, -1]
StartPointer = 3
HeapPointer = 4

LinkedListData = [5, 6, 7, 9, None, None, None]
LinkedListPointer = [-1, 0, 1, 2, 5, 6, -1]

while StartPointer != -1:
    print (LinkedListData[StartPointer])
    StartPointer = LinkedListPointer[StartPointer]

