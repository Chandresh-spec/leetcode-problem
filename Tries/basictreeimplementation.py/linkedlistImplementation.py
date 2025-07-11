
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def Preorder(root):
    if root is None:
        return 
    
    print(root.data,end=" ")
    Preorder(root.left)
    Preorder(root.right)



def Inorder(root):
    if root is None:
        return 
    Inorder(root.left)
    print(root.data,end=" ")
    Inorder(root.right)





def Postorder(root):
    if not root:
        return 
    
    Postorder(root.left)
    Postorder(root.right)
    print(root.data,end=" ")


from collections import deque
def LevelOrder(root):
    queue=deque([root])
    while queue:
        temp=queue.popleft()
        print(temp.data,end=" ")
        
        if temp.left:
            queue.append(temp.left)
        
        if temp.right:
            queue.append(temp.right)

from collections import deque
def Insert(root,data):
    queue=deque([root])
    while queue:
        temp=queue.popleft()
    
        if temp.left:
           queue.append(temp.left)
        else:
            temp.left=Node(data)
            break
    
        if temp.right:
            queue.append(temp.right)
        else:
            temp.right=Node(data)
            break



def DeleteDeepest(root,key):
    queue=deque([root])
    while queue:
       temp=queue.popleft()
       if key is temp:
          temp=None    
          return
    
       if temp.left:
          if temp.left is key:
              temp.left=None
              return
          else:
              queue.append(temp.left)
    
       if temp.right:
          if temp.right is key:
             temp.right=None
             return
          else:
              queue.append(temp.right)


  



def DeleteNode(root,key):
    if not root:
        return "Tree is None"
    
    if root.left is None and root.right is None:
        if root.data==key:
            return None
        return root.data
       
    queue=deque([root])
    hold=None
    temp=None
    while queue:
        temp=queue.popleft()

        if temp.data==key:
            hold=temp
        
        if temp.left:
             queue.append(temp.left)
        
        if temp.right:
            queue.append(temp.right)
    
    if hold:
        hold.data=temp.data
        DeleteDeepest(root,temp)
        
        
        














N1=Node(10)
N1.left=Node(20)
N1.right=Node(30)
N1.left.left=Node(40)
N1.left.right=Node(50)
N1.right.left=Node(60)
N1.right.right=Node(70)


Preorder(N1)
print()
Inorder(N1)
print()
Postorder(N1)
print()

Insert(N1,80)
Insert(N1,90)
Insert(N1,190)
LevelOrder(N1)
print()

DeleteNode(N1,30)

DeleteNode(N1,20)

LevelOrder(N1)
print()
