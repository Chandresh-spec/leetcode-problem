# Generate Binary Strings Without Consecutive 1s
# Subscribe to TUF+

# Hints
# Company
# Given an integer n, return all binary strings of length n that do not contain consecutive 1s. Return the result in lexicographically increasing order.



# A binary string is a string consisting only of characters '0' and '1'.


# Example 1

# Input: n = 3

# Output: ["000", "001", "010", "100", "101"]

# Explanation: All strings are of length 3 and do not contain consecutive 1s.

# Example 2

# Input: n = 2

# Output: ["00", "01", "10"]

# Constraints

# 1 <= n <=



class Solution:
    def generateBinaryStrings(self, n):
        # Your code goes here
        ans=[]
        def helper(cur):
            if len(cur)==n:
                ans.append(cur)
                return 
            
            helper(cur+'0')

            if cur=="" or cur[-1]=="0":
                helper(cur+'1')
            
        
        helper("")
        return ans