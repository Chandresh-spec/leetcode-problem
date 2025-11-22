# 1901. Find a Peak Element II
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

# Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

# You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

# You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

# Example 1:



# Input: mat = [[1,4],[3,2]]
# Output: [0,1]
# Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
# Example 2:



# Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
# Output: [1,1]
# Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 500
# 1 <= mat[i][j] <= 105
# No two adjacent cells are equal.


def check(row,col,n,m,mat):
    if col>0 and mat[row][col]< mat[row][col-1] :
        return False
    
    if row>0 and mat[row][col]< mat[row-1][col] :
        return False
    
    if col<n-1 and mat[row][col]< mat[row+1][col] :
        return False
    
    if col<n-1 and mat[row][col]< mat[row][col+1] :
       return False
    

    return True
    
    
    
    
    




def findPeak(mat):
    n=len(mat)
    m=len(mat[0])
    for i in range(n):
        for j in range(m):
            if check(i,j,n,m,mat):
                return [i,j]
    

    return -1



mat = [[1,4],[3,2]]

print(findPeak(mat))






from typing import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:


        def findmaxi(col,mat):
            maxi=mat[0][col]
            row=0
            for i in range(1,len(mat)):
                if mat[i][col]>maxi:
                    maxi=mat[i][col]
                    row=i
            return row
                

        rows=len(mat)
        col=len(mat[0])
        lb,ub=0,col-1

        while lb <= ub :
            mid=(ub+lb)//2

            maxi=findmaxi(mid,mat)

            
            left=mat[maxi][mid-1]if mid-1 >= 0 else -1
            right=mat[maxi][mid+1] if mid+1< col else -1

            if  mat[maxi][mid]>left and mat[maxi][mid]>right:
                return [maxi,mid]
            
            elif left > mat[maxi][mid]:
                ub=mid-1
            
            else:
                lb=mid+1
        

        return [-1,-1]
