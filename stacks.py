Stackarray = [None for i in range (10)]

Basepointer = 0 
Toppointer = -1
Stackful = 9

def isFull():
    global Toppointer
    if Toppointer >= Stackful:
        return True
    else:
        return False

def isEmpty ():
    global Toppointer 
    if Toppointer < Basepointer:
        return True
    else:
        return False


def Pop():
    global Toppointer
    popping = input("Do you want to pop(Yes/No): ")
    if popping == "Yes":
        if isEmpty():
            print ("Stack is empty, cannot pop anymore")
        else:
            print ("Item is already popped")
            popped = Stackarray [Toppointer]
            Toppointer = Toppointer - 1
            return popped


def Push():
    global Toppointer
    no1 = int(input("Enter the number to add: "))
    if isFull():
        print ("The stack is already full, cannot push")
    else:
        Toppointer = Toppointer + 1
        Stackarray[Toppointer] = no1
        print ("The item is being pushed")


choice ="Yes"
while choice != "No":
    choice = input("Do you want to push or pop (Push/Pop): ")
    if choice == "Push":
        Push()
    else:
        Pop()