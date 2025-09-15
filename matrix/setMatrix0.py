def setZeros(matrix):
    n=len(matrix)
    m=len(matrix[0])
    row=[0]*n
    col=[0]*m

    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
            
        
    for i in range(n):
        for j in range(m):
            if row[i] or row[j]:
                matrix[i][j]=0
            
    return matrix



matrix = [[1,1,1],[1,0,1],[1,1,1]]


print(setZeros(matrix))