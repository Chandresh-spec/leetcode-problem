# class Node:
#     def __init__(self,data):
#         self.next=None
#         self.data=data


    


# class LinkedList:
#     def __init__(self):
#         self.head=None

    

#     def insertion_at_beg(self,data):
#         nb=Node(data)
#         nb.next=self.head
#         self.head=nb
    

#     def insert_at_end(self,data):
#         ne=Node(data)
#         temp=self.head

#         while temp.next:
#             temp=temp.next

#         temp.next=ne
    

#     def insert_at_middle(self,data,index):
#         nm=Node(data)
#         temp=self.head
#         for i in range(index-1):
#             temp=temp.next
        
#         nm.next=temp.next
#         temp.next=nm


#     def delete_at_beg(self):
#         if self.head is None:
#             return None
        
#         if self.head.next is None:
#              self.head=None
#              return None
        
#         self.head=self.head.next



#     def delete_at_end(self):
       
#         temp=self.head
#         if temp is None or temp.next is None:
#             return None
        

#         while temp.next.next:
#             temp=temp.next
        
#         temp.next=None


#     def delete_at_middle(self,index):
#         temp=self.head

#         for i in range(index-1):
#             temp=temp.next

        
#         temp.next=temp.next.next




# def traversal(root):
#     temp=root


#     while temp:
#         print(temp.data,end="->")

#         temp=temp.next




# n1=Node(10)

# h1=LinkedList()
# h1.head=n1

# n1.next=Node(20)
# n1.next.next=Node(30)
# n1.next.next.next=Node(40)
# h1.insertion_at_beg(5)
# h1.insertion_at_beg(1)
# h1.insert_at_end(50)
# h1.insert_at_end(50)
# h1.insert_at_middle(42,2)
# h1.insert_at_middle(4,3)
# h1.delete_at_beg()
# h1.delete_at_beg()
# h1.delete_at_end()
# h1.delete_at_end()
# h1.delete_at_middle(2)
# h1.delete_at_middle(0)
# traversal(h1.head)



class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
    



class Linkedlist:
    def __init__(self):
        self.head=None


    
    def traversal(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        
    
    def length(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        
        return count
        

    
    def insert_at_beg(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            return

        node.next=self.head
        self.head=node

    
    def insert_at_end(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            return
        
        temp=self.head

        while temp.next:
            temp=temp.next
        

        temp.next=node

    
    def insert_at_spec(self,index,value):
        n=self.length()-1
        if index >n:
            print(f"plz correctly enter the index current length of the linkedlist is",{n+1})
            return 
        node=Node(value)
        if index ==0:
            self.insert_at_beg(value)
            return 
        temp=self.head
        for _ in range(index-1):
            temp=temp.next
        

        node.next=temp.next
        temp.next=node
    


    def remove_at_beg(self):
        self.head=self.head.next

    
    def remove_at_end(self):
        temp=self.head

        while temp.next.next:
            temp=temp.next
        
        temp.next=None
    

    def remove_at_spec(self,index):
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        
        temp.next=temp.next.next
    








# l1=Linkedlist()
# l1.insert_at_beg(10)
# l1.insert_at_end(30)
# l1.insert_at_end(60)
# l1.insert_at_spec(2,50)
# l1.remove_at_beg()
# l1.remove_at_end()
# l1.remove_at_spec(1)
# l1.traversal()



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    


class DoublyLinkedlist:
    def __init___(self):
        self.head=None
        self.tail=None

    

    def forwardtraversal(self):
        temp=self.head
        while temp:
             print(temp.data,end="->")
             temp=temp.next
    

    def length(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        
        return count


    

    def backwardtraversal(self):
        print()
        temp=self.tail

        while temp:
            print(temp.data,end="->")
            temp=temp.prev



    
    def insert_at_beg(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        

        nb=Node(data)
        nb.next=self.head
        self.head.prev=nb
        self.head=nb



    def insert_at_end(self,data):
        if self.tail is None:
            self.tail=Node(data)
            return
        
        ne=Node(data)
        self.tail.next=ne
        ne.prev=self.tail
        self.tail=ne





    def insert_at_spec(self,index,data):
        np=Node(data)
        if self.head and self.tail is None:
            self.head=np
            self.tail=np
            return
        
        len=self.length()-1
        if index >len:
            return "index not found"
        
        if index==0:
            self.insert_at_beg(data)
            return
        
        if index ==len:
            self.insert_at_end(data)
            return
        temp=self.head
        for _ in range(index-1):
            temp=temp.next
        

        np.next=temp.next
        temp.next.prev=np
        temp.next=np
        np.prev=temp
        
       


    def remove_at_beg(self):
        if self.head is None:
            return "linkedlist is empty"
        
        temp=self.head
        self.head=self.head.next
        self.head.prev=None
        temp.next=None

    def remove_at_end(self):
        if self.tail is None:
            return "linkedlist is empty"
        
        temp=self.tail
        self.tail=self.tail.prev
        self.tail.next=None
        temp.prev=None


    def remove_at_spec(self,index):
        if self.head is None:
            return "linkedlist is empty"
        
        if index==0:
            self.remove_at_beg()
            return
        
        len=self.length()
        if index==len:
            self.remove_at_end()
            return
        
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        

        temp.next=temp.next.next
        temp.next.prev=temp

        
    def pallindrome(self):
        
        fast=slow=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        
        
        prev=None
        temp=self.head
        while prev!=slow:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        

        back=slow

        if not fast:
            slow=slow.next
        
        
        while slow and back:
            if slow.data!=back.data:
                return False
            
            slow=slow.next
            back=back.next
        
        return True





    def helper(self,temp):
            if temp.next is None:
                new_head=temp
                return new_head
            

            New_head=self.helper(temp.next)
            front=temp.next
            front.next=temp
            temp=None
            return New_head.data
        
        
n1=Node(10)
l1=DoublyLinkedlist()
l1.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1

n3=Node(30)
n2.next=n3
n3.prev=n2

n4=Node(30)
n4.prev=n3
n3.next=n4
l1.tail=n4


# l1.insert_at_beg(5)
# l1.insert_at_beg(7)
# l1.insert_at_end(50)
l1.insert_at_end(20)
l1.insert_at_end(10)

# l1.insert_at_spec(7,23)
# l1.remove_at_beg()
# l1.remove_at_beg()
# l1.remove_at_beg()
# l1.remove_at_end()
# l1.remove_at_end()
# l1.remove_at_spec(2)
# l1.remove_at_spec(1)
# l1.forwardtraversal()
# l1.backwardtraversal()
# print(l1.pallindrome())
print(l1.helper(l1.head))