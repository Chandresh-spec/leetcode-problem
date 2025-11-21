# 240. Search a 2D Matrix II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -109 <= target <= 109




from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==target:
                    return True
        

        return False
    






class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def call(matrix,row,n,target):
            lb,ub=0,n-1

            while lb <= ub :
                mid=(ub+lb)//2

                if matrix[row][mid]==target:
                    return True
                
                if  matrix[row][mid]>target:
                    
                    ub=mid-1
                else:
                    lb=mid+1
                    
            
            return False




        n=len(matrix[0])
        m=len(matrix)


        for i in range(m):
            if matrix[i][0]<= target <= matrix[i][n-1]:
                if call(matrix,i,n,target):
                    return True
        

        return False





class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        row=0
        col=m-1

        while row< n and col>=0:
            current=matrix[row][col]

            if current==target:
                return True
            
            elif current>target:
                col-=1
            else:
                row+=1
        
        return False