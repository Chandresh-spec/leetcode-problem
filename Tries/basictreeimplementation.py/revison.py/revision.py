class Tree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data


def Preorder(root):
    if not root:
        return
    
    print(root.data,end=" ")
    Preorder(root.left)
    Preorder(root.right)


def Inorder(root):
    if not root:
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


def IterativePreoder(root):
    stack=[root]
    ans=[]
    while stack:
        temp=stack.pop()
        ans.append(temp.data)

        if temp.right:
            stack.append(temp.right)
        
        if temp.left:
            stack.append(temp.left)
        
    return ans

def IterativeInorder(root):
    stack=[]
    cur=root
    ans=[]

    while stack or cur:
        while  cur:
            stack.append(cur)
            cur=cur.left
        
        temp=stack.pop()
        ans.append(temp.data)
        cur=temp.right
        
    
    print(ans)


def IterativePostorder(root):
    stack=[]
    cur=root
    ans=[]

    while cur or stack:
        while cur:
            
            stack.append(cur)
            cur=cur.left
        
        if stack[-1].right :
            stack.append()
            cur=stack[-1]
        else:
            temp=stack.pop()
            ans.append(temp.data)
            cur=stack[-1]



        
        
        



    



t1=Tree(10)
t1.left=Tree(20)
t1.right=Tree(30)
t1.left.left=Tree(40)
t1.left.right=Tree(50)
t1.right.left=Tree(60)
t1.right.right=Tree(70)

Preorder(t1)
print()
Inorder(t1)
print()
Postorder(t1)  
print()

print(IterativePreoder(t1))

print()
IterativeInorder(t1)