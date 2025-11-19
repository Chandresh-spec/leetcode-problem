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
        
    def add1(self):
        temp=self.head
        st=""
        while temp:
            st+=str(temp.data)
            temp=temp.next
        
        num=int(st)+1
        st=str(num)

        i=0
        temp=self.head
        a=None
        while temp and i <len(st):
            temp.data=st[i]
            i+=1
            a=temp
            temp=temp.next
            
        
        if st[i]:
            a.next=Node(0)

        

        
    


h1=Linkedlist()

n1=Node(9)







h1.head=n1



print(h1.add1())
h1.traversal()