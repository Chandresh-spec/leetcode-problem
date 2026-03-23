from collections import deque
class BT:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    



def preorder(root):
    if root is None:
        return False
    
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)




def postorder(root):
    if root is None:
        return
    

    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")


def levelorder(root):
    q=deque()
    q.append(root)
    while q :
        item=q.popleft()

        print(item.data)

        if item.left:
            q.append(item.left)
        
        if item.right:
            q.append(item.right)
        


# def insertion(root,data):
#     if root is None:
#         return True
    
#     if root.left is None:
#         root.left=BT(data)
#         return
#     else:
#         insertion(root.left,data)
    
#     if root.right is None:
#         root.right=BT(data)
#         return
#     else:
#         insertion(root.right,data)
    
    


def delete(root,data):
    q=deque()
    q.append(root)
    target_node=None
    while q :
        item=q.popleft()

        if item.data==data:
            target_node=item

        if item.left:
            q.append(item.left)
        
        if item.right:
            q.append(item.right)
    

    target_node.data=item.data
    delete_node(root,item)



def delete_node(root,data):
    q=deque()
    q.append(root)
    while q :
        item=q.popleft()

        if item.data==data:
            target_node=item

        if item.left==data:
            item.left=None
            break
        else:
            q.append(item.left)
        
        if item.right==data:
            item.right=None
            break
        else:
            q.append(item.right)
    

    
    












n1=BT(10)
n1.left=BT(20)
n1.right=BT(30)
n1.left.left=BT(40)
n1.left.right=BT(50)
n1.right.left=BT(60)
n1.right.right=BT(70)
# preorder(n1)
# inorder(n1)
# postorder(n1)
delete(n1,50)
levelorder(n1)

