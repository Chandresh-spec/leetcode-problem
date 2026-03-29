def inorderTraversal(root):
        ans=[]
        cur=root

        while cur:
            if not cur.left:
                ans.append(cur.val)
                cur=cur.right
            else:
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                
                if prev.right is None:
                    prev.right=cur
                    cur=cur.left
                
                else:
                    prev.right=None
                    ans.append(cur.val)
                    cur=cur.right
               
        
        return ans
            
