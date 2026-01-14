# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q=deque([root])
        real_ans=[]
        rotate=True

        while q:
            ans=[]
            for i in range(len(q)):
                temp=q.popleft()

                ans.append(temp.val)

                if temp.left:
                    q.append(temp.left)
                
                if temp.right:
                    q.append(temp.right)
            


            if not rotate:
                ans.reverse()
                real_ans.append(ans)
                rotate=True
            else:
                real_ans.append(ans)
                rotate=False
            

        return real_ans
