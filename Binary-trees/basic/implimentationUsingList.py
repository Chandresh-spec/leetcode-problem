

# def preorder(arr,index):
#     if  index >=len(arr) or not arr[index] :
#         return
    
#     print(arr[index])
#     preorder(arr,2*index+1)
#     preorder(arr,2*index+2)



# arr=[10,20,30,40,50,60,70]
# print(preorder(arr,0))




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

postorder(t1.root)

postorder2(t1.root)

