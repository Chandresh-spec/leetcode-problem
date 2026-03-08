class Node:
    def __init__(self,data):
        self.next=None
        self.data=data


    


class LinkedList:
    def __init__(self):
        self.head=None

    

    def insertion_at_beg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    

    def insert_at_end(self,data):
        ne=Node(data)
        temp=self.head

        while temp.next:
            temp=temp.next

        temp.next=ne
    

    def insert_at_middle(self,data,index):
        nm=Node(data)
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        
        nm.next=temp.next
        temp.next=nm


    def delete_at_beg(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
             self.head=None
             return None
        
        self.head=self.head.next



    def delete_at_end(self):
       
        temp=self.head
        if temp is None or temp.next is None:
            return None
        

        while temp.next.next:
            temp=temp.next
        
        temp.next=None


    def delete_at_middle(self,index):
        temp=self.head

        for i in range(index-1):
            temp=temp.next

        
        temp.next=temp.next.next




def traversal(root):
    temp=root


    while temp:
        print(temp.data,end="->")

        temp=temp.next




n1=Node(10)

h1=LinkedList()
h1.head=n1

n1.next=Node(20)
n1.next.next=Node(30)
n1.next.next.next=Node(40)
h1.insertion_at_beg(5)
h1.insertion_at_beg(1)
h1.insert_at_end(50)
h1.insert_at_end(50)
h1.insert_at_middle(42,2)
h1.insert_at_middle(4,3)
h1.delete_at_beg()
h1.delete_at_beg()
h1.delete_at_end()
h1.delete_at_end()
h1.delete_at_middle(2)
h1.delete_at_middle(0)
traversal(h1.head)
