from collections import deque



class Node:
    def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None



class Tree:
    def __init__(self):
        self.root=None

    


# def preorder(root):
#     stack=[root]
#     while not stack:
#         ele=stack.pop()

#         print(ele.data)

#         if ele.right:
#             stack.append(ele.right)

#         if ele.left:
#             stack.append(ele.left)


# using two stack representation
def postorder(root):
    stack1=[root]
    stack2=[]

    while  stack1:
        node=stack1.pop()
        stack2.append(node.data)

        if node.left:
           stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    
    stack2.reverse()
    print(stack2)


# using two stack representation
def postorder2(root):
    last_visited=None
    cur=root
    stack=[root]

    while cur or stack:
        if cur.left:
            stack.append(cur)
            cur=cur.left


        else:
            peek=stack[-1]

            if peek.right and last_visited!=peek.right:
                cur=peek.right

            else:
                print(peek.data)
                last_visited=stack.pop()


def findMaxDepth(root):
    if root is None:
        return 0
    
    l=findMaxDepth(root.left)
    r=findMaxDepth(root.right)
    return max(l,r)+1


# using level order
def findmaxDepth(root):
    q=deque([root])
    count=0

    while q :
        for i in range(len(q)):
            current=q.popleft()

            if current.left:
                q.append(current.left)

            if current.right:
                q.append(current.right)
        
    
        count+=1
    
    return count


t1=Tree()
n1=Node(10)
t1.root=n1
n1.left=Node(20)
n1.right=Node(30)
n1.left.left=Node(40)
n1.left.right=Node(50)
n1.right.left=Node(60)
n1.right.right=Node(70)

# preorder(t1.root)


print(findMaxDepth(t1.root))

print(findmaxDepth(t1.root))