
# Insert a given node in BST
# Delete a node in BST
# Kth Smallest and Largest element in BST
# Check if a tree is a BST or not
# LCA in BST
# Construct a BST from a preorder traversal
# Inorder successor and predecessor in BST

# FAQs
# Contest

# Heaps

# Graphs

# Dynamic Programming

# Tries

# Strings (Advanced Algo)

# Maths
# Track
# Command Palette
# Search for a command to run...

# Set your roadmap and track your progress here


# FindBorderBarSize
# Inorder successor and predecessor in BST
# Subscribe to TUF+

# Hints
# Company
# Given the root node of a binary search tree (BST) and an integer key. Return the Inorder predecessor and successor of the given key from the provided BST.



# Note: key will always present in given BST.



# If predecessor or successor is missing then return -1.


# Example 1

# Input : root = [5, 2, 10, 1, 4, 7, 12] , key = 10

# Output : [7, 12]

# Explanation :



# Example 2

# Input : root = [5, 2, 10, 1, 4, 7, 12] , key = 12

# Output : [10, -1]

# Explanation :



# Now your turn!

# Input : root = [5, 2, 10, 1, 4, 7, 12] , key = 1

# Output:

# # Pick your answer




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def succPredBST(self, root, key):
        #your code goes here
        self.p,self.s=-1,-1

        def helper(root):
            if root is None:
                return
            
            if root.data< key and root.data>self.p:
                self.p=root.data
            
            if root.data > key and  self.s<root.data:
                self.s=root.data

            
            helper(root.left)
            helper(root.right)
        helper(root)
        return [self.p,self.s]
            
          
        
    


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def succPredBST(self, root, key):
        #your code goes here
        self.p,self.s=-1,-1
        cur=root

        while cur :
            if key <cur.data:
                self.s=cur.data
                cur=cur.left
            if key > cur.data:
                self.p=cur.data
                cur=cur.right
            
            else:
                temp=cur.left
                while temp:
                    self.p=temp.data
                    temp=temp.right
                
                temp=cur.right
                while temp:
                    self.s=temp.data
                    temp=temp.left
                
                break
        return[self.p,self.s]
