# 222. Count Complete Tree Nodes
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.
# Seen this question in a real interview before?
# 1/5




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root) -> int:
          

        if not root:
            return 0
        
        l=self.leftTree(root)
        b=self.RightTree(root)

        if l==b:
            return (1<<l)-1

        return 1+self.countNodes(root.left)  + self.countNodes(root.right)

        





    def leftTree(self,root):
            height=0
            while root:
                root=root.left
                height+=1
            
            return height
        

    def RightTree(self,root):
            height=0
            while root:
                root=root.right
                height+=1
            
            return height
    
        
        
            

            


        
        