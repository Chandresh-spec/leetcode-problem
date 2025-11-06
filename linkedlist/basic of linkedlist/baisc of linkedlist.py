# What is a Linked List?

# A linked list is a linear data structure where elements (called nodes) are stored in separate objects and linked together using pointers (or references). Each node typically contains:

# data (value)

# next (pointer/reference to the next node)

# Contrast with an array:

# Array: contiguous block of memory; index-based random access (O(1)). Resizing may be expensive (copy).

# Linked list: nodes scattered in memory; traversal required for access (O(n)), but insert/delete at arbitrary positions (when you have pointer) is cheap: O(1) to insert/delete at head or given node (if pointer available).

# Key tradeoffs (arrays vs linked lists)

# Access by index: array O(1), linked list O(n).

# Insertion/deletion: array O(n) (shift elements), linked list O(1) if position/node is known.

# Memory overhead: linked lists use extra memory for pointers.

# Cache locality: arrays are contiguous → faster due to CPU cache; linked lists have poor locality.

# Node structure (conceptual)




# implementation of linkedlist




class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


class Linkedlist:
    def __init__(self):
        self.head=None
    


    def traversal(self):
        if not self.head:
            return None
        
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
    

    def insert_at_beg(self,data):
        node=Node(data)

        node.next=self.head

        self.head=node

    
    def insert_at_end(self,data):
        node=Node(data)
        if  self.head is None:
            return node
        
        temp=self.head
        while temp.next:
            temp=temp.next
        
        temp.next=node
    
    def insert_at(self,data,index):
        node=Node(data)
        if  self.head is None:
                return node
        
        temp=self.head
        for i in range(1,index-1):
            temp=temp.next


        node.next=temp.next
        temp.next=node
        

            
    


h1=Linkedlist()

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)


h1.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

h1.insert_at_beg(0)
h1.insert_at_beg(-1)
h1.insert_at_end(6)
h1.insert_at_end(7)
h1.insert_at(10,3)
h1.insert_at(10,2)
h1.traversal()




