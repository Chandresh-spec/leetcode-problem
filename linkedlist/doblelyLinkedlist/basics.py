class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    

class Dlinkedlist1:
    def __init__(self):
        self.head=None
    

    def forward__traversal(self):
        if self.head is None:
            return None
        

        temp=self.head

        while temp:
            print(temp.data,end="->")
            temp=temp.next
    

    def backward_traversal(self):

        if self.head is None:
            return None
        

        temp=self.head

        while temp.next:
            temp=temp.next
        a=temp
        while a:
            print(a.data,end="->")
            a=a.prev


    def insert_at_beg(self,data):
        nb=Node(data)
        if self.head is None:
            return nb
        

        nb.next=self.head
        self.head.prev=nb
        self.head=nb
    

    def insert_at_end(self,data):
        ne=Node(data)
        if self.head is None:
            return ne
        
        temp=self.head

        while temp.next:
            temp=temp.next
        
        temp.next=ne
        ne.prev=temp
    

    def insert_at_middle(self,index,data):
        np=Node(data)
        if self.head is None:
            return np
        
        temp=self.head
        for i in range(1,index-1):
            temp=temp.next
        
        np.next=temp.next
        temp.next.prev=np
        temp.next=np
        np.prev=temp


n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)



dll=Dlinkedlist1()

dll.head=n1
n1.next=n2

n2.next=n3
n2.prev=n1


n3.next=n4
n3.prev=n2

n4.next=n5
n4.prev=n3

n5.prev=n4


dll.insert_at_beg(5)
dll.insert_at_beg(1)
dll.insert_at_beg(6)
dll.insert_at_end(70)
dll.insert_at_end(80)
dll.insert_at_end(90)

dll.insert_at_middle(2,10)
dll.insert_at_middle(1,10)
dll.forward__traversal()

print()
dll.backward_traversal()






