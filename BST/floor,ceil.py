# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        #your code goes here
        temp=root
        ciel,floor=-1,-1

        while temp:

            if key < temp.data:
                ciel=temp.data
                temp=temp.left

            
            else:
                floor=temp.data
                temp=temp.right
        
        return [floor,ciel]