queue = [i for i in range (10)]

print (queue)

Size = 10
Toppointer = 9
Frontpointer = 0
Rearpointer = 9

def dequeue():

    dequeued = queue[Frontpointer]
    Size = Size - 1
    if Frontpointer == len (queue) - 1 and Size != 10:
        Frontppointer = 0 
    else:
        Frontpointer = Frontpointer + 1
    return dequeued

import stacks

         
 

print (new_queue)
