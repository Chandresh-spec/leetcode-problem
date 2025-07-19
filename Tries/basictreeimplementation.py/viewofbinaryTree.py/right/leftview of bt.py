# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue=deque([(root,(0))])

        hashmap={}

        while queue:
            temp,x=queue.popleft()

            hashmap[x]=temp.val

            if temp.left:
                queue.append((temp.left,(x+1)))
            
            if temp.right:
                queue.append((temp.right,(x+1)))
        
        ans=[]
        for x in sorted(hashmap.keys()):
            ans.append(hashmap[x])
        
        return ans


        

        