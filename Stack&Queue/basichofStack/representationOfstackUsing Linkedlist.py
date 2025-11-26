class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None



class Linkedlist:
    def __init__(self):

        self.head=None

    

    def tarversal(self):
        temp=self.head

        while temp:
            print(temp.data,end="\n")
            temp=temp.next
        
    

    def push(self,data):
        if self.head is None:
            nb=Node(data)
            self.head=nb
            return
        
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def pop(self):
        if self.head is None:
            return "stack is empty"
        

        self.head=self.head.next
    

    def peek(self):
       if self.head is None:
           return "stack is  empty"
       print(self.head.data)
        


    

h1=Linkedlist()
h1.push(10)
h1.push(20)
h1.push(30)
h1.pop()
h1.tarversal()
h1.peek()
        