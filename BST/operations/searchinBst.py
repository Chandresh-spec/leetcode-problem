# 700. Search in a Binary Search Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107
 

# Seen this question in a real interview before?
# # 1/5




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def searchBST(self,root,val):
#         temp=root

#         while temp:
#             if temp.val==val:
#                 return temp
            
#             elif val < temp.val:
#                 temp=temp.left







class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



class BST:
    def __init__(self):
        self.root=None




def traversal(root):
    if root is None:
        return 
    
    

    print(root.data)
    traversal(root.left)
    traversal(root.right)
    


def search(temp,key):
    

    if temp is None:
        return False
    

    if temp.data==key:
        return True
    
    if temp.data>key:
        return search(temp.left,key)

    return search(temp.right,key)




def insertion(temp,key):
    if temp is None:
        return Node(key)
    
    if temp.data>key:
         temp.left=insertion(temp.left,key)
        
    else:
        temp.right=insertion(temp.right,key)
    
    return  temp





t1=BST()
n1=Node(8)
t1.root=n1

n1.left=Node(4)
n1.left.left=Node(2)
n1.left.right=Node(6)
n1.right=Node(12)
n1.right.left=Node(10)
n1.right.right=Node(14)
# traversal(t1.root)
# print(search(t1.root,6))
insertion(t1.root,11)
print(traversal(t1.root))