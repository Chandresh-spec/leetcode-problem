# 540. Single Element in a Sorted Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 



from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)-1
        if len(nums)==1:
            return nums[0]
        
        if nums[0]!= nums[1]:
            return nums[0]
        
        if nums[n] != nums[n-1]:
            return nums[n]
        

        lb=1
        ub=len(nums)-2
        while lb <= ub:
            mid=(ub+lb)//2

            if nums[mid] != nums[mid-1]  and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            if (mid % 2 ==1 and nums[mid]== nums[mid-1]) or(mid % 2==0 and nums[mid]==nums[mid+1]):
               lb=mid+1
            
            else:
                ub=mid-1
        
        return -1