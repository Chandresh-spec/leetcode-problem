# 1248. Count Number of Nice Subarrays
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

 

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
 

from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def counsubarray(nums,k):
            sum_of=0
            odd_count=0
            st=0
            for i in  range(len(nums)):
                if nums[i] %2==1:
                    odd_count+=1

                    while odd_count>k:
                        if nums[st]%2==1:
                           odd_count-=1
                        st+=1
                
                sum_of+=i-st+1

            return sum_of
        

        return counsubarray(nums,k) - counsubarray(nums,k-1)

        
        


       
       