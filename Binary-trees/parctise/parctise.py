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

    
    






arr = [1, 2, 3, 4, 5, 6]
hashmap={}

for i in arr:
    if i%2==0:
        if "even" not in hashmap:
            hashmap["even"]=[]
        
        hashmap["even"].append(i)
    else:
        if "odd" not in hashmap:
            hashmap["odd"]=[]
        
        hashmap["odd"].append(i)



print(hashmap)    








n1=BT(3)
n1.left=BT(9)
n1.right=BT(20)
# n1.left.left=BT(40)
# n1.left.right=BT(50)
n1.right.left=BT(15)
n1.right.right=BT(7)
# preorder(n1)
# inorder(n1)
# postorder(n1)
# delete(n1,50)
# levelorder(n1)
# print(inorder2(n1))
verticaltraversal(n1)





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


data = [
    (0, 0, 3),
    (-1, 1, 9),
    (1, 1, 20),
    (0, 2, 15),
    (2, 2, 7)
]

hashmap={}
for i in data:
    x,y,z=i

    if x not in hashmap:
        hashmap[x]={}

    if y not in hashmap[x]:
        hashmap[x][y]=[]
    
    hashmap[x][y].append(z)


print(hashmap)
    
