class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    


class Linkedlist:
    def __init__(self):
        self.head=None

    
    def traversal(self):
        temp=self.head
        while temp:
           print(temp.data,end="<-")
           temp=temp.next

    

    def enqueue(self,data):
        nb=Node(data)

        if self.head is None:
            self.head=nb
        
        else:
            a=self.head

            while a.next:
                a=a.next
            
            a.next=nb
    
    def dequeue(self):
        if self.head is None:
            return "queue is empty"
        if self.head.next is None:
            self.head=None
            return 
        self.head=self.head.next
    

    def peek(self):
        return self.head.data
    


    def length(self):
        count=0
        temp=self.head

        while temp:
            temp=temp.next
            count+=1
    
        return count
        




l1=Linkedlist()
l1.enqueue(10)
l1.enqueue(20)
l1.enqueue(30)
l1.dequeue()
l1.dequeue()
l1.dequeue()



l1.traversal()
# print()
# print(l1.peek())
# 
# print(l1.length())