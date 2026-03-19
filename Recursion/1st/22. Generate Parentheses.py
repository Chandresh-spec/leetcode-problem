
# Code
# 22. Generate Parentheses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8








from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def helper(open1,close,n,cur):
            if len(cur)==2*n:
                ans.append(cur)
                return
            
            if open1 < n :
                helper(open1+1,close,n,cur+'(')
            
            if close <open1 :
                helper(open1,close+1,n,cur+')')
        

        helper(0,0,n,'')
        return ans
