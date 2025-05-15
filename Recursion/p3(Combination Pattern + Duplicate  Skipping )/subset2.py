# 90. Subsets II
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


def subset2(arr):
    ans=[]
    def helper(index,ds):
        ans.append(ds[:])
        if len(arr)==index:
            return
        
        
        for  i in range(index,len(arr)):
            if i!=index and arr[i]==arr[i-1]:
                continue
            ds.append(arr[i])
            helper(i+1,ds)
            ds.pop()
    helper(0,[])   
    return ans

arr=[0]
print(subset2(arr))
    