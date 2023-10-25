# . Implement a queue data structure in Python using a list.
# Include enqueue, dequeue, and peek operation


"""


Que data structure in python
que follows a firts in firts out rule

queeue key terms

enqueue - is putting items in the queue
dequeue - removing items from queue

basic operations of queue
Enqueue  - adding an element to  end of queue
Dequeue - removing an element from front of  queue
isEmpty  - check if queue id empty
isFull - check if  queueid full
peek - get  the value of the front queu without removing it

""" 

#Implementation of  queue in python

class Queue:
    
    def __init__(self):
        self.queue = []
 
 
 
#adding an element to a queue
def enqueue(self, item):
    self.queue.append(item)
    
    



#removing an element from a queue
def dequeue(self):
    if len(self.queue) < 1:
        return None
    return self .queue.pop(0)



#Display the queue
def display(self):
    print(self.queue)



def size(self):
    return len(self.queue)
      
    
    
    
    
    q  = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    
    
    q.display()
    
    q.dequeue()
    
    
    
    print("After removing the element")
    q.display(  )
    
    
    
    
    
    