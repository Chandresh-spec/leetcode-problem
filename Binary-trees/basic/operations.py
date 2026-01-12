from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class Tree:
    def __init__(self):
        self.root=None


def preorder(root):
    if root is None:
        return
    
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def insertion(root,data):
    q=deque([root])

    while q:
        current=q.popleft()


        if not current.left:
            current.left=Node(data)
            return
        
        else:
            q.append(current.left)


        if not current.right:
            current.right=Node(data)
            return
        else:
            q.append(current.right)


def delete_targeted_node(root,target):
    q=deque([root])
    parent_last=None
    current=None
    target_node=None

    while q:
        current=q.popleft()
        if current.data==target:
            target_node=current


        if current.left:
           q.append(current.left)
           parent_last=current



        if current.right:
            q.append(current.right)
            parent_last=current


    if target_node is None:
        return root
    
    target_node.data=current.data


    if parent_last.left==current:
        parent_last.left=None

    if parent_last.right==current:
        parent_last.right=None
    



n1=Node(10)
s1=Tree()
s1.root=n1

n1.left=Node(20)
n1.right=Node(30)
n1.left.left=Node(40)
n1.left.right=Node(50)
n1.right.left=Node(60)
n1.right.right=Node(70)

insertion(s1.root,80)

delete_targeted_node(s1.root,30)
preorder(s1.root)

