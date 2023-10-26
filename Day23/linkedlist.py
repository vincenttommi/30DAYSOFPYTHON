"""
linked list - are data structures that stores data inform of a chain
node - an element in each linked-list

prons of linked list
1 You can add and remove elements quilcky
2 Linked list  don't require  a fixed size or initial size due to chainlike structure

# cons
# 1 occuppies more memory compared to  an array.
# 2 search operations on a linked list are very slow

# """

#examples of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def  __init(...)
    def append(...)
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

            self.head = new_node
        
        
        
        
# #invoking values as arguments to a LinkedList
# e1 = Node(1)
# e2 = Node(2)
 
        
        
        
# ll = LinkedList(e1)  


class LinkedList:
    def __init(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        current = self.head
        prev = None

        if current is not None and current.value == value:
            self.head = current.next
            return

        while current is not None:
            if current.value == value:
                break
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

                
              
              
        