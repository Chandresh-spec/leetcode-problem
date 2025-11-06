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
       

    def remove_at_st(self):
        if self.head is None:
            return None
        

        if self.head.next is None:
             self.head=None
             return None
    

        temp=self.head
        self.head=temp.next
        temp.next=None

    

    def remove_from_end(self):
        if self.head is None or self.head.next is None:
            print("None")
        
        a=self.head.next
        temp=self.head


        while a.next:
            a=a.next
            temp=temp.next
        
        temp.next=None
    

    def remove_from_middle(self,index):

        if self.head is None:
            return None
        
        temp=self.head
        for i in range(1,index-1):
            temp=temp.next
        

        temp.next=temp.next.next
    

    def search(self,value):
        if not self.head:
         return None
     
        temp=self.head
        while temp:
            if temp.data==value:
                print(True)
            temp=temp.next
        print(False)

l1=Linkedlist()

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)


l1.head=n1
n1.next=n2
n2.next=n3
n3.next=n4



l1.remove_at_st()
l1.search(99)

l1.traversal()