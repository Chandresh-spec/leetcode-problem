# 40. Combination Sum II
# Solved
# Medium
# Topics
# Companies
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

def combination2(arr,target):
    ans=[]
    arr.sort()
    
    def helper(index,ds,target):
        if target==0:
            ans.append(ds[:])
            return
        
        for i in range(index,len(arr)):
            if i> index and arr[i]==arr[i-1]:
                continue

            if arr[i]>target:
                break
            ds.append(arr[i])
            helper(i+1,ds,target-arr[i])
            ds.pop()
    helper(0,[],target)
    return ans

arr=[10,1,2,7,6,1,5]
target=8
print(combination2(arr,target))

