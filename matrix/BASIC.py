# a  matrix is collection  of number arranged in rectnagular array in rows and colums


# m-> rows
# n-> colums


# denoted by m*n

mat=[[1,3,4],
     [4,8,9],
     [7,6,3]]


print(mat)



# tarversal :- row major and colum major method

#ROW MAJOR

m=len(mat)
n=len(mat[0])


for i in range(m):
    for j in range(n):
        print(mat[i][j],end=" ")



#COLUMN MAJOR METHOD

print()
for i in range(n):
    for j in range(m):
        print(mat[j][i],end=" ")


    

