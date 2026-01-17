class Node:
     def __init__(self,data):
          self.data=data
          self.left=None
          self.right=None
    
class Tree:
     def __init__(self):
          self.root=None




def allRootToLeaf(root):
        #your code goes here
        ans=[]
        def helper(root,ds):
            if root is None:
                return 
            
            
            if root.left is None and root.right is  None:
                ans.append(ds[:])
            else:
                ds.append(root.data)
                helper(root.left,ds)
                helper(root.right,ds)
                ds.pop()
            
            
        

        helper(root,[])
        return ans



t1=Tree()
n1=Node(1)
t1.root=n1
n1.left=Node(2)
n1.right=Node(3)
n1.left.right=Node(5)
n1.right.right=Node(3)
n1.right.right=Node(60)

print(allRootToLeaf(t1.root))