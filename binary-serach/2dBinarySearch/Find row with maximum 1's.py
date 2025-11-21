# Find row with maximum 1's


# 0

# 100
# Easy

# Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order, find the index of the row with the maximum number of ones.

# If two rows have the same number of ones, consider the one with a smaller index. If no 1 exists in the matrix, return -1.


# Examples:
# Input : mat = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]

# Output: 0

# Explanation: The row with the maximum number of ones is 0 (0 - indexed).

# Input: mat = [ [0, 0], [0, 0] ]

# Output: -1

# Explanation: The matrix does not contain any 1. So, -1 is the answer.




# def Matrix(nums):
    # maxi=-1
    # n=len(nums[0])
    # m=len(nums)
    # for  i in range(n):
        # count=0
        # for j in range(m):
            # if nums[i][j]==1:
                # count+=1
            # 
        # 
        # maxi=max(maxi,count)
    # 
    # return maxi
# 
# 
# mat = [ [0, 0, 1], [0, 1, 1], [0, 1, 1] ]

# print(Matrix(mat))



# 
# def BinaryMatrix(nums):
    # maxi=0
    # n=len(nums[0])
    # m=len(nums)
    # for i in range(m):
        # low=0
        # high=n-1
# 
        # while low<= high:
            # mid=(high+low)//2
# 
            # if nums[i][mid]==1:
                # high=mid-1
            # else:
                # low=mid+1
            # 
        # count=n-low
        # maxi=max(maxi,count)
    # 
    # return -1  if maxi==0 else maxi
# 
# 
# 
# mat = [ [0, 0, 1], [0, 1, 1], [0, 1, 1] ]
# print(BinaryMatrix(mat))
# 






def solveNQueens(n):
    def backtrack(row):
        if row == n:
            for r in board:
                print(" ".join(r))
            print()     
            return

        for col in range(n):
            if col in columns or (row + col) in diag1 or (row - col) in diag2:
                continue

            board[row][col] = "Q"
            columns.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            backtrack(row + 1)

            board[row][col] = "."
            columns.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

    board = [["."] * n for _ in range(n)]
    columns = set()
    diag1 = set()
    diag2 = set()

    backtrack(0)



n = int(input("Enter Board Size (n>=4): "))
solveNQueens(n)
