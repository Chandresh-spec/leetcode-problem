from collections import deque
class BT:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    



def preorder(root):
    if root is None:
        return False
    
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)




def postorder(root):
    if root is None:
        return
    

    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")


def levelorder(root):
    q=deque()
    q.append(root)
    while q :
        item=q.popleft()

        print(item.data)

        if item.left:
            q.append(item.left)
        
        if item.right:
            q.append(item.right)
        


# def insertion(root,data):
#     if root is None:
#         return True
    
#     if root.left is None:
#         root.left=BT(data)
#         return
#     else:
#         insertion(root.left,data)
    
#     if root.right is None:
#         root.right=BT(data)
#         return
#     else:
#         insertion(root.right,data)
    
    


def delete(root,data):
    q=deque()
    q.append(root)
    target_node=None
    while q :
        item=q.popleft()

        if item.data==data:
            target_node=item

        if item.left:
            q.append(item.left)
        
        if item.right:
            q.append(item.right)
    

    target_node.data=item.data
    delete_node(root,item)



def delete_node(root,data):
    q=deque()
    q.append(root)
    while q :
        item=q.popleft()

        if item.data==data:
            target_node=item

        if item.left==data:
            item.left=None
            break
        else:
            q.append(item.left)
        
        if item.right==data:
            item.right=None
            break
        else:
            q.append(item.right)



def inorder2(root):
        if root is None:
            return []
        stack=[root]
        cur=None
        ans=[]


        while stack or cur:
            while cur:
                stack.append(cur)
                
                cur=cur.left
            
            temp=stack.pop()
            ans.append(temp.data)
            cur=temp.right
        
        return ans
    
    

from collections import deque
def verticaltraversal(root):
    q=deque()
    q.append((root,0,0))

    while q:
        temp,x,y=q.popleft()

        print((temp.data,x,y))


        if temp.left:
            q.append((temp.left,x+1,y-1))
        
        if temp.right:
            q.append((temp.right,x+1,y+1))

    
    





def topView(self, root):
        #your code goes here

        q=deque()
        q.append((root,0))

        nodes={}
        ans=[]
        while q:
            temp,x=q.popleft()

            if x not in nodes:
                nodes[x]=temp.data

            if temp.left:
                q.append((temp.left,x-1))
            
            if temp.right:
                q.append((temp.right,x+1))
        

        
       
        for x in sorted(nodes.keys()):
            ans.append(nodes[x])
        

        return ans


def bottomView(self, root):
        #your code goes here
        
        q=deque()
        q.append((root,0))

        nodes={}
        ans=[]
        while q:
            temp,x=q.popleft()

            
            nodes[x]=temp.data

            if temp.left:
                q.append((temp.left,x-1))
            
            if temp.right:
                q.append((temp.right,x+1))
        

  
       
        for x in sorted(nodes.keys()):
            ans.append(nodes[x])
        

def rightview(root):
            if root is None:
                return []
            
            q=deque()
            q.append((root,0))

            nodes={}
            ans=[]
            while q:
                temp,x=q.popleft()

            
                nodes[x]=temp.val

                if temp.left:
                    q.append((temp.left,x+1))
                
                if temp.right:
                    q.append((temp.right,x+1))
            

    
        
            for x in sorted(nodes.keys()):
                ans.append(nodes[x])
            

            return ans

def allRootToLeaf(root):
        #your code goes here

        ans=[]
        def helper(ds,root):
            if root is None:
                return
            
            

            ds.append(root.data)
            helper(ds,root.left)
            helper(ds,root.right)
            ds.pop()
            
            if not root.left and not root.right:
                ans.append(ds[:])
        helper([],root)
        return ans





def widthOfBinaryTree(root):
        q=deque()
        q.append((root,0))
        max_depth=0
        while q:
            end_node=0
            _,start_node=q[0]
            for i in range(len(q)):

                temp,x=q.popleft()
                end_node=x

                if temp.left:
                    
                    q.append((temp.left,x*2))
                    
                
                if temp.right:
    
                    q.append((temp.right,x*2+1))
            
            max_depth=max(max_depth,end_node-start_node+1)
        

        return max_depth





def checkChildrenSum(root):

        def helper(root):
            if root is None:
                return True

            # ✅ leaf node
            if not root.left and not root.right:
                return True
            
            data1 = root.left.val if root.left else 0
            data2 = root.right.val if root.right else 0

            if data1 + data2 != root.val:
                return False
            
            # ✅ check both sides
            return helper(root.left) and helper(root.right)

        return helper(root)



def distancek(root,k,target):
    q=deque()
    q.append(root)
    hashmap={}

    while q :
            temp=q.popleft()
          
            if temp.left:
               hashmap[temp.left]=temp
               q.append(temp.left)
            

            if temp.right:
                 hashmap[temp.right]=temp
                 q.append(temp.right)
            
    
    
    q=deque()
    q.append(target)
    visited={}
    distance=0
    ans=[]

    while q:
        if k>=distance:
            for i in range(len(q)):
                
                    temp=q.popleft()
                    visited[temp]=True
                
                   
                    if temp.left and temp.left not in visited:
                        q.append(temp.left)
                      
                             
                            
                    if temp.right and temp.right not in visited:
                        q.append(temp.right)
                        
                        
                    
                    upper=hashmap.get(temp,None)

                    if upper and upper not in visited:
                        q.append(upper)
                    
                    if distance==k:
                         ans.append(temp.data)
                       
            distance+=1
            
        else:
             break
    print(ans)



def TimetoBurnTree(root,target):
     
    q=deque()
    q.append(root)
    hashmap={}
    while q :
            temp=q.popleft()
            if temp.left:
               hashmap[temp.left]=temp
               q.append(temp.left)
            
            if temp.right:
                hashmap[temp.left]=temp
                q.append(temp.right)
    

    q=deque([target])
    visited=set([target])
    count=0

    while q :
        for i in range(len(q)):
                temp=q.popleft()
                visited.add(temp)

                if temp.left and temp.left not in visited:
                   q.append(temp.left)
                
                if temp.right and  temp.right not in visited:
                     q.append(temp.right)
                
                upper=hashmap.get(temp,None)

                if upper and upper not in visited:
                     q.append(upper)
        count+=1
    
    return count
            
                

            

     
        

n1=BT(3)
n1.left=BT(5)
n1.right=BT(1)
n1.left.left=BT(6)
n1.left.right=BT(2)
n1.right.left=BT(0)
n1.right.right=BT(8)
n1.left.right.left=BT(7)
n1.left.right.right=BT(4)
# print(allRootToLeaf(n1))
# print(widthOfBinaryTree(n1))
# print(checkChildrenSum(n1))
# print(distancek(n1,2,n1.left))
print(TimetoBurnTree(n1,n1))
# preorder(n1)
# inorder(n1)
# postorder(n1)
# delete(n1,50)
# levelorder(n1)
# print(inorder2(n1))
# verticaltraversal(n1)





# data = [
#     ("Alice", "Math", 90),
#     ("Alice", "Science", 85),
#     ("Bob", "Math", 78)
# ]

# hashmap={}
# for item in data:
#     x,y,z=item
#     if y not in hashmap:
#         hashmap[y]={}

#     hashmap[y][x]=z

    


# print(hashmap)


# words = ["apple", "ant", "bat", "ball", "cat"]
# hashmap={}
# for i in words:
#     x=i[0]

#     if x not in hashmap:
#         hashmap[x]=[]
    
#     hashmap[x].append(i)

# print(hashmap)


# data = [
#     (0, 0, 3),
#     (-1, 1, 9),
#     (1, 1, 20),
#     (0, 2, 15),
#     (2, 2, 7)
# ]

# hashmap={}
# for i in data:
#     x,y,z=i

#     if x not in hashmap:
#         hashmap[x]={}

#     if y not in hashmap[x]:
#         hashmap[x][y]=[]
    
#     hashmap[x][y].append(z)


# print(hashmap)
    
