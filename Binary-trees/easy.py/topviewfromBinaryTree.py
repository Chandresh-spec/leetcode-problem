# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def topView(self, root):
        #your code goes here

        q=deque()
        mapp={}
        q.append((root,0))

        while q:
            temp,x=q.popleft()


            if x not in mapp:
                mapp[x]=temp.data

            
            if temp.left:
                q.append((temp.left,x-1))
            
            if temp.right:
                q.append((temp.right,x+1))
            
        ans=[]

        for item in sorted(mapp):
            ans.append(mapp[item])
        

        return ans