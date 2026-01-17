# Minimum time taken to burn the BT from a given Node
# Hard

# Hints
# Company
# Given a target node data and a root of binary tree. If the target is set on fire, determine the shortest amount of time needed to burn the entire binary tree.



# It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.


# Example 1

# Input : root = [1, 2, 3, 4, null, 5, 6, null, 7]. target = 1

# Output : 3

# Explanation : The node with value 1 is set on fire.

# In 1st second it burns node 2 and node 3.

# In 2nd second it burns nodes 4, 5, 6.

# In 3rd second it burns node 7.



# Example 2

# Input : root = [1, 2, 3, null, 5, null, 4], target = 4

# Output : 4

# Explanation : The node with value 4 is set on fire.

# In 1st second it burns node 3.

# In 2nd second it burns node 1.

# In 3rd second it burns node 2.

# In 4th second it burns node 5.



# Now your turn!

# Input : root = [1, 2, 3, 6, 5, 8, 4], target = 4


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def timeToBurnTree(self, root, start):
        #your code goes here
        hashmap={}
        startnode=None
        def helper(root,prev):
            nonlocal startnode
            if root is None:
                return
            
            hashmap[root]=prev

            if start==root.data:
                startnode=root

            helper(root.left,root)
            helper(root.right,root)
        
        helper(root,None)
        

        q=deque([(startnode,0)])
        vis=set([startnode])
        burn=0

        while q:
            node,burn=q.popleft()

            for val in (node.left,node.right,hashmap[node]):
                if val and  val not in vis:
                    vis.add(val)

                    q.append((val,burn+1))
            
        
        return burn

            




