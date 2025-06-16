class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    


def preorder(root):
    if not root:
        return
    print(root.data,end="->")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end="->")
    inorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end="->")


from collections import deque
def levelorder(root):
    if not root:
        return 
    
    queue=deque([root])
    while queue:
            q1=queue.popleft()
            print(q1.data,end="->")
        
            if q1.left:
                queue.append(q1.left)
            
            if q1.right:
                queue.append(q1.right)


def insertnode(root,data):
    if not root:
        return Node(data)
    
    queue=deque([root])
    while queue:
            q1=queue.popleft()
            print(q1.data,end="->")
            if not q1.left:
                q1.left=Node(data)
                break
            else:
                queue.append(q1.left)
            if not q1.right:
                q1.right=Node(data)
                break
            else:
                queue.append(q1.right)
    

    





node1=Node(10)
node1.left=Node(20)
node1.right=Node(30)
node1.left.left=Node(40)
node1.left.right=Node(50)
node1.right.left=Node(60)
node1.right.right=Node(70)

preorder(node1)
print()
inorder(node1)
print()
postorder(node1)

print()

insertnode(node1,80)

levelorder(node1)


