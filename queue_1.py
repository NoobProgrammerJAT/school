Queuearray = [None for i in range (10)]

Frontpointer = 0
RearPointer = -1
Size = len(Queuearray)
Full = 10
def isFull():
    if Size >= Full:
        return True
    else:
        return False 
    
def isEmpty():
    if Size <= 0:
        return True
    else:
        return False 
    
def Enqueue():
    global Frontpointer
    global RearPointer
    no1 = int(input("Enter the number to add: "))
    if Frontpointer >= 9:
        if isFull():
            print ("The queue is already full, cannot enqueue anymore.")
        else: 
            RearPointer = 0
            Queuearray[RearPointer] = no1
