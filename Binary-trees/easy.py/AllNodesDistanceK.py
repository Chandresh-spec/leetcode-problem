
class Node:
     def __init__(self,data):
          self.data=data
          self.left=None
          self.right=None
    
class Tree:
     def __init__(self):
          self.root=None



from collections import deque

def distanceK(root,target,k):
        hashmap={}
        def helper(root,prev):
            if root is None:
                return
            
            hashmap[root]=prev

            helper(root.left,root)
            helper(root.right,root)
        
        helper(root,None)
        
        q=deque([(target,0)])
        vis=set([target])

        ans=[]
        while q:
            node,dis=q.popleft()

            if dis==k:
                ans.append(node.val)
                continue
            
            if dis>k:
                break
            

            for val in(node.left,node.right,hashmap[node]):
                if val and val not in vis:
                    vis.add(val)

                    q.append((val,dis+1))
        

        return ans
    




t1=Tree()
n1=Node(1)
t1.root=n1
n1.left=Node(2)
n1.right=Node(3)
n1.left.right=Node(5)
n1.right.right=Node(3)
n1.right.right=Node(60)

print(distanceK(t1.root,))