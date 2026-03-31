class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    


def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def search(root,target):

    if root is None:
        return
    while root :
        if target==root.data:
            return True
        if target < root.data:
            root=root.left
        else:
            root=root.right
        
    return False

def insertion(root,data):
    if root is None:
        return Node(data)
    
    while root:
        if data<root.data:
            if root.left:
              root=root.left
            else:
                root.left=Node(data)
                break
                
        else:
            if root.right:
               root=root.right
            else:
                root.right=Node(data)
                break

def RecursiveInsertion(root,data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left=RecursiveInsertion(root.left,data)
    else:
        root.right=RecursiveInsertion(root.right,data)
    

    return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValidBST(root):
        # q=deque()

        # q.append((root,float('-inf'),float('inf')))

        # while q:
        #     temp,mini,maxi=q.popleft()


        #     if mini >= temp.val or  temp.val>=maxi:
        #         return False
            
        #     if temp.left:
        #         q.append((temp.left,mini,temp.val))
            
        #     if temp.right:
        #         q.append((temp.right,temp.val,maxi))
    
        # return True


        def helper(root,mini,maxi):
            if root is None:
                return True
            
            if mini >= root.val or  root.val>=maxi:
                return False
            

            return helper(root.left,mini,root.val) and helper(root.right,root.val,maxi)
        

        return helper(root,float('-inf'),float('inf'))

        





n1=Node(10)
n1.left=Node(5)
n1.left.left=Node(4)
n1.left.right=Node(6)
n1.right=Node(15)
n1.right.left=Node(11)
n1.right.right=Node(30)

print(search(n1,85))
insertion(n1,3)
RecursiveInsertion(n1,7)
preorder(n1)
