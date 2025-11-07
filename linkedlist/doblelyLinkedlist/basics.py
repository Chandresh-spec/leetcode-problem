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
            self.head=nb
            return 
        

        nb.next=self.head
        self.head.prev=nb
        self.head=nb
    

    def insert_at_end(self,data):
        ne=Node(data)
        if self.head is None:
            self.head=ne
            return 
        
        temp=self.head

        while temp.next:
            temp=temp.next
        
        temp.next=ne
        ne.prev=temp
    

    def insert_at_middle(self,index,data):
        np=Node(data)
        if self.head is None:
            self.head=np
            return 
        
        temp=self.head
        for i in range(1,index-1):
            temp=temp.next
        
        np.next=temp.next
        temp.next.prev=np
        temp.next=np
        np.prev=temp

# ____________________________________________________________________________________________________________________________________________________________________________________________________
    # remove operations


    def remove_from_beg(self):
        if self.head is None:
            return 
        
        if self.head.next is None:
            self.head =None
            return 
        
        self.head=self.head.next
        self.head.prev=None

    


    def remove_from_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head=None
            return
        a=self.head.next
        temp=self.head

        while a.next:
            a=a.next
            temp=temp.next
        

        temp.next=None
        a.prev=None
    

    def reverse_ddl(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        
        a=None
        temp=self.head

        while temp:

            next_node=temp.next
            temp.next=a
            temp.prev=next_node

            a=temp
            temp=next_node
            


    def remove_from_middle(self,index):
        if self.head is None:
            return None
        
        temp=self.head
        for i in range(1,index-1):
            if temp.next is None:
                break
            temp=temp.next
        
        del_node=temp.next
        if del_node is None:
            return
        
        temp.next=del_node.next
        if del_node.next:
            del_node.next.prev=temp


        



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

# _____________________________________________________________________________________________________________________________________

dll.remove_from_beg()
dll.remove_from_beg()
dll.remove_from_end()
dll.remove_from_end()
dll.remove_from_end()
dll.remove_from_middle(2)
dll.remove_from_middle(3)
dll.remove_from_middle(3)
dll.reverse_ddl()
dll.forward__traversal()
print()
# dll.backward_traversal()
# 





