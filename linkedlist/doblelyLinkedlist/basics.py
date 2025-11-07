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


dll.forward__traversal()
print()
dll.backward_traversal()



