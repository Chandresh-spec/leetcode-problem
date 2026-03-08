class Node:
    def __init__(self,data):
        self.next=None
        self.data=data


    


class LinkedList:
    def __init__(self):
        self.head=None



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
traversal(h1.head)
