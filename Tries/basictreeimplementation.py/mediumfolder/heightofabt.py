class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    

def helper(root):
    if not root:
        return 0
    l=helper(root.left)
    b=helper(root.right)
    return max(l,b)+1


    



N1=Node(3)
N1.left=Node(9)
N1.right=Node(20)
N1.right.left=Node(1)
N1.right.right=Node(7)
print(helper(N1))
