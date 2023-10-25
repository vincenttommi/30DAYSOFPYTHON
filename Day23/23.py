"""

stack Data structure 
is a linear structure that  follows principle of Last in First out
means the last  inserted element is the first to come out
 
 principles of stack
 
 push -putting an item on top of  a stack
 pop - removing an item from a stack
 
 
 
 Basic operations of stack
 push - add an element to top of the stack
 pop - remove  an element from top of the stack
 isEmpty - check if the stack is empty
 isFull - Check if the stack is full
 peek - getting the  value of the top element without removing it
 
 
 
 working stack data structure
 top - used to keep track of the top element
 when initialising stack we  use -1 to check if the stack is empty
 when pushing an element we increase the value of top
 Before pushing we check if the stack is already full
 Before popping we check if the stack is already empty  
 

"""
#Stack implementation in python

#creating a stack 

def create_stack():
    stack = []
    return stack



# creating an empty stack
def check_empty(stack):
    return len(stack) == 0


#adding items  into  the stack
def push(stack, item):
    stack.append(item)
    print('pushed item:' + item)
    
    print(stack)
    
    
    
    
    
#Removing  an element from the stack
def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"
    
    return stack.pop()




stack = create_stack()
push(stack,str(1))
push(stack, str(2))
push(stack, str(3)) 
push(stack, str(4))

print("popped item:" + pop(stack))
print("stack after popping an element:" + str(stack))