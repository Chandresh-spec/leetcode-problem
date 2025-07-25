# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def lowestCommonAncestor(root, p, q) :
        def helper(root,p,q):
            if not root:
                return

            
            
            if root==p or root==q:
                return root
            
            l= helper(root.left,p,q)
            b=helper(root.right,p,q)


            if l and b:
               return root
            

            return l if l else b
        return helper(root,p,q)

            