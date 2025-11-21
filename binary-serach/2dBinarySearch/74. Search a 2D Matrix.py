# 74. Search a 2D Matrix
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0])
        m=len(matrix)
        for i in range(m):
            for j in range(n):
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
                
                elif matrix[row][mid]>target:
                    ub=mid-1
                else:
                    lb=mid+1
            return False
        n=len(matrix[0])
        m=len(matrix)
        for i in range(m):
            if matrix[i][0]<=target <= matrix[i][n-1]:
                return call(matrix,i,n,target)
            
        return False
            