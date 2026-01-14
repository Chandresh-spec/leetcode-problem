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
            if root is None:
                return  0

            l=max(0,helper(root.left))
            if l<0:
                l=0
            r=max(0,helper(root.right))
            

            self.maxi=max(self.maxi,root.val+l+r)

            return root.val+max(l,r)

        helper(root)
        return self.maxi