from collections import defaultdict,deque
def vertical(root):

    node=defaultdict(lambda:list())
    queue=deque(root,(0,0))


    while queue:
        temp,(x,y)=queue.popleft()


        node[x][y].append(temp.val)

        if temp.left:
            queue.append(temp.left,(x-1,y+1))
        
        if temp.right:
            queue.append(temp.right,(x+1,y+1))
    
    ans=[]
    for x in sorted(node):
        col=[]
        for y in sorted(node[x]):
            col+=sorted([node[x][y]])
        ans.append(col)
    
    return ans
        
        




