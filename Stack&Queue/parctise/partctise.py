# class Stack:
    # def __init__(self):
        # self.stack=[]
    # 
# 
# 
    # def __str__(self):
        # val=[str(x) for x in reversed(self.stack)]
        # return "\n".join(val)
    # 
# 
    # def isempty(self):
        # if  self.stack==[]:
            # return True
        # return False
    # 
# 
# 
    # def push(self,val):
        # self.stack.append(val)
    # 
# 
    # def pop(self):
        # if self.isempty():
            # return "stack is empty"
        # 
        # self.stack.pop()
    # 
    # def peek(self):
        # return self.stack[-1]   
# 
# 
# 
# 
# s1=Stack()
# print(s1.isempty())
# s1.push(10)
# s1.push(20)
# s1.push(30)
# 
# s1.pop()
# print(s1)
# print(s1.peek())
# print("-"*30)
# 
# class Node:
    # def __init__(self,data,next=None):
        # self.data=data
        # self.next=None
# 
# 
    # 
# class LinkedList:
    # def __init__(self):
        # self.head=None
    # 
# 
# 
    # 
    # 
    # 
    # 
# 
# 
    # def traversal(self):
        # if self.head is None:
            # print("stack is empty")
        # temp=self.head
        # while temp:
            # print(temp.data,end="<-")
            # temp=temp.next
# 
    # 
# 
    # def isempty(self):
        # if self.head is None:
            # return True
        # return False
    # 
# 
    # def push(self,val):
        # nb=Node(val)
        # if self.head is None:
            # self.head=nb
            # return
        # 
        # nb.next=self.head
        # self.head=nb
# 
# 
    # def pop(self):
        # if self.head is None:
            # print("empty stack")
            # return
        # if self.head.next is None:
            # self.head=None
            # return
        # self.head=self.head.next
# 
    # def peek(self):
        # return self.head.data
# 
# 
# 
# 
# 
# 
# l1=LinkedList()
# l1.push(10)
# l1.push(20)
# l1.push(30)
# l1.pop()
# l1.pop()
# 
# l1.traversal()
# 
# print("-"*30)



from collections import deque

class Queue:
    def __init__(self):
        self.q=deque()
    


    def __str__(self):
       val=[str(x) for x in self.q]
       return "\n".join(val)

    

    def isempty(self):
        if not  self.q:
            return False
        
        return True
    

    def push(self,data):
        self.q.append(data)

        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())



    def pop(self):
        self.q.popleft()
    

    def peek(self):
        return self.q[0]
    





q1=Queue()
q1.push(10)
q1.push(20)
q1.push(30)
q1.pop()
print(q1)

