# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root) :
        if not root:
            return []
        

        queue=deque([root])
        ds=[]
        flag=True
        while queue:
            ans=[]
            n=len(queue)
            for i in range(n):
                temp=queue.popleft()
                ans.append(temp.val)

                if temp.left:
                    queue.append(temp.left)
                
                if temp.right:
                    queue.append(temp.right)
                
                
            if not flag:
                ans.reverse()

            
            ds.append(ans)
            flag=not flag
        
        
        

        return ds