# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q) :
        def helper(p,q):
            
            if not p and not q:
                return True

            if not p or not q :
                return False
                
            if p.val!=q.val:
                return False

            return helper(p.left,q.left) and  helper(p.right,q.right)
           
            
        return helper(p,q)

p = [1,2,3]
q = [1,2,3]
print(isSameTree(p,q))