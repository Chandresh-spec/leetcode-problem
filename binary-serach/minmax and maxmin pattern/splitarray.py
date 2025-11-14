# 410. Split Array Largest Sum
# Attempted
# Hard
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.








from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        def check(nums,j):
            partition=1
            subarray=0
            for i in range(len(nums)):
                if nums[i]+subarray<=j:
                    subarray+=nums[i]
                else:
                    partition+=1
                    subarray=nums[i]
            
            return partition==k



        



        low=max(nums)
        high=sum(nums)

        for i in range(low,high+1):
            if check(nums,i):
                return i
        
        return  low