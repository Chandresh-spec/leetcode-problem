# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter=0
        def helper(root):
            if not root:
                return 0

            l=helper(root.left)
            b=helper(root.right)
            self.diameter= max(self.diameter,l+b)
            return max(l,b)+1
        helper(root)
        return self.diameter