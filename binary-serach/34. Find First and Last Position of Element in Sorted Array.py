# 34. Find First and Last Position of Element in Sorted Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

class Solution:
    def searchRange(nums,target: int):
        def binary_search(nums,target):
            lb=0
            ub=len(nums)-1
            ans=-1

            while lb <= ub:
                mid=(ub+lb)//2

                if nums[mid]==target:
                    ans=mid
                    ub=mid-1
                elif  nums[mid] > target:
                    ub= mid-1

                else:
                    lb=mid+1
            return ans
        

        def binary_search2(nums,target):
            lb=0
            ub=len(nums)-1
            ans=-1

            while lb <= ub:
                mid=(ub+lb)//2

                if nums[mid]==target:
                    ans=mid
                    lb=mid+1
                elif  nums[mid] > target:
                    ub= mid-1

                else:
                    lb=mid+1
            return ans
        first=binary_search(nums,target)
        second=binary_search2(nums,target)
        
        return[first,second]
    

    nums = [5,7,7,8,8,10]
    target = 8

    

                    
        