

def preorder(arr,index):
    if  index >=len(arr) or not arr[index] :
        return
    
    print(arr[index])
    preorder(arr,2*index+1)
    preorder(arr,2*index+2)



arr=[10,20,30,40,50,60,70]
print(preorder(arr,0))




class Node:
    def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None



class Tree:
    def __init__(self):
        self.root=None

    


def traversal(root):
    stack=[root]
    while not stack:
        ele=stack.pop()

        print(ele.data)

        if ele.right:
            stack.append(ele.right)

        if ele.left:
            stack.append(ele.left)






t1=Tree()
n1=Node(10)
t1.root=n1
n1.left=Node(20)
n1.right=Node(30)
n1.left.left=Node(40)
n1.left.right=Node(50)
n1.right.left=Node(40)
n1.right.right=Node(40)

traversal(t1.root)

