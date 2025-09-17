def sprial_mat(matrix):
    n=len(matrix)
    m=len(matrix[0])-1

    lb=0
    ub=n
    uub=m
    llb=0
    ans=[]

    for i in range(lb,ub+1):
        ans.append(matrix[lb][i])
    
    lb+=1


    for i in range(lb+1,uub):
        ans.append(matrix[i][uub])
    
    ub-=1

    

    for i in range(uub-1,-1,llb):
        ans.append(matrix[uub][i])


    

    return ans














matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
print(sprial_mat(matrix))