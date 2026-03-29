
class Solution:
    def preorderTraversal(root):
        cur=root
        ans=[]

        while cur:
            if cur.left is None:
                ans.append(cur.val)
                cur=cur.right
            
            else:
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                
                if prev.right is None:
                    ans.append(cur.val)
                    prev.right=cur
                    
                    cur=cur.left
                
                else:
                    prev.right=None
                    cur=cur.right
        
        return ans