# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      
        def helper(root):
            if not root:
                return 0
            

            l= helper(root.left)
            if l==-1:
                return -1
            b= helper(root.right)
            if b==-1:
                return -1

            if abs(l-b)>1:
                return -1

            return max(l,b)+1

        return helper(root)!= -1
           

        
            
            