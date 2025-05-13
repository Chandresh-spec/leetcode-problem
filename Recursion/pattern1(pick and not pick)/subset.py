# 78. Subsets
# Solved
# Medium
# Topics
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

def subset(arr):
    ans=[]
    def helper(index,count):
        if index==len(arr):
            ans.append(count)
            return 
        
        helper(index+1,count+arr[index])
        helper(index+1,count)
    
    helper(0,0)
    return ans

arr=[2,3]
print(subset(arr))