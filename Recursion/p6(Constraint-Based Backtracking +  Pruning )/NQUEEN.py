
# Solved
# Hard
# Topics
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]
 



from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
            self.ans=[]
            def helper(col,board,left,upper_diag,lower_diag):
                if col==n:
                    self.ans.append([''.join(row) for row in board])
                    return
                for i in range(n):
                       if left[i]==0  and upper_diag[i+col]==0 and lower_diag[n-1+col-i]==0:
                            board[i][col]='Q'
                            left[i],upper_diag[i+col],lower_diag[n-1+col-i]=1,1,1

                            helper(col+1,board,left,upper_diag,lower_diag)
                            board[i][col]='.'
                            left[i],upper_diag[i+col],lower_diag[n-1+col-i]=0,0,0



            board=[['.' for i in range(n)]for i in range(n)]
            left=[0]*n
            upper_diag=[0]*(2*n-1)
            lower_diag=[0]*(2*n-1)
            helper(0,board,left,upper_diag,lower_diag)
            return self.ans
            