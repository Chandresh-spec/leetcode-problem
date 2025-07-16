# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        self.maxi=float('-inf')  
        def helper(root):
            if not root:
                return 0
            
            l=max(0,helper(root.left))
            b=max(0,helper(root.right))

            count=l+b+root.val
            self.maxi=max(count,self.maxi)

            return root.val+max(l,b)
        
        helper(root)
        return self.maxi