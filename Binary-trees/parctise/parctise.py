from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def inorder(root):
    cur=root
    stack=[]

    while stack or cur:
        
        while cur:
            
            stack.append(cur)
            cur=cur.left

        
        temp=stack.pop()
        print(temp.data)
        cur=temp.right



def  postorder(root):
    pass





def preorder(root):
    ans=[]
    queue=deque()
    queue.append(root)
    cur=root

    while queue or cur:

        while cur.left!=None:
            cur=cur.left

        ans.append(cur.data)
        cur=cur.right
    
    return ans
    # if root is None:
    #     return 
    
    # print(root.data,end=" ")
    # preorder(root.left)
    # preorder(root.right)



def levelorder(root):
    q=deque()
    q.append(root)
    
    while  q:
        temp=q.popleft()

        print(temp.data,end=" ")

        if temp.left:
            q.append(temp.left)
        
        if temp.right:
            q.append(temp.right)


n1=Node(10)
n1.left=Node(20)
n1.right=Node(30)
n1.left.left=Node(40)
n1.left.right=Node(50)
n1.right.left=Node(60)
n1.right.right=Node(70)

inorder(n1)

# levelorder(n1)