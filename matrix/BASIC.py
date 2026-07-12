# # a  matrix is collection  of number arranged in rectnagular array in rows and colums


# # m-> rows
# # n-> colums


# # denoted by m*n

# mat=[[1,3,4],
#      [4,8,9],
#      [7,6,3]]


# print(mat)



# # tarversal :- row major and colum major method

# # #ROW MAJOR

# # m=len(mat)
# # n=len(mat[0])


# # for i in range(m):
# #     for j in range(n):
# #         print(mat[i][j],end=" ")



# # #COLUMN MAJOR METHOD

# # print()
# # for i in range(n):
# #     for j in range(m):
# #         print(mat[j][i],end=" ")


    


# # nums=[[1,3,4],
# #      [4,8,9],
# #      [7,6,3]]
# # n=len(nums[0])
# # m=len(nums)


# # for  r in range(m):
# #     for c in range(n):
# #         print(nums[r][c],end=" ")
    
# #     print()


# # print("_"*4)

# # for  c in range(n):
# #     for r in range(3):
# #         print(nums[r][c],end=" ")
    
# #     print()






# def setZeroes(matrix) -> None:

#     n=len(matrix[0])
#     m=len(matrix)
#     cols=matrix[0][0]
#     # c=[0]*n
#     # r=[0]*m

#     # for i in range(m):
#     #     for j in range(n):
#     #         if matrix[i][j]==0:
#     #             c[j]=1
#     #             r[i]=1
    

#     # for i in range(m):
#     #     for j in range(n):
#     #         if c[j]==1 or r[i]==1:
#     #             matrix[i][j]=0
    

#     # return matrix
#     for i in range(m):
#         for j in range(n):
#             if  matrix[i][j]==0:
#               if j ==0:
#                 cols=0
#               else:
#                 matrix[0][j]=0
#               matrix[i][0]=0
    
#     for i in range(1,m):
#         for j in range(1,n):
#             if matrix[0][j]==0 or matrix[i][0]==0:
#                 matrix[i][j]=0
    
#     for i in range(1,n):
#        if cols==0 or 
       
    
#     # for c in range(m):
#     #     if matrix[0][0]==0:
#     #         for i in range(m):
#     #             matrix[i][0]==0
        

#     for i in matrix:
#         print(i,end=" ")
#         print()
    
    



# matrix = matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# print(setZeroes(matrix))
        


# def RotateImage(matrix):
   
#     n=len(matrix[0])
#     m=len(matrix)
#     # arr=[[0 for _ in range(n)]for _ in range(n)]
#     # for i in range(m):
#     #     for j in range(n):
#     #         arr[j][n-i-1]=matrix[i][j]
    

#     # return arr

#     for i in range(n):
#         for j in range(n):
#             matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        

#     for i in matrix:
#             print(i,end=" ")
#             print()


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(RotateImage(matrix))




def setmatrix(matrix):
        n=len(matrix[0])
        m=len(matrix)

        first_row=False
        first_column=False  
        for j in range(n):

            if matrix[0][j]==0:
                first_row=True
                break
        
        for i in range(m):
            if matrix[i][0]==0:
                first_column=True
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            

        if first_row:
            for j in range(n):
                matrix[0][j]=0
        

        if first_column:
            for i in range(m):
                matrix[i][0]=0
        


        return matrix

              
    
  
        for i in range(m):
            for j in range(n):
                print(matrix[i][j],end=" ")
            print()





matrix=[[1,1,1,1],[1,0,1,1],[0,1,1,1],[1,1,0,1]]
print(setmatrix(matrix))
                    
