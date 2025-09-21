# 560. Subarray Sum Equals K
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107





class Solution:
    def subarraySum(nums,k) -> int:
        prefix_sum=0
        count=0
        hashmap={0:1}
        for  i in range(len(nums)):
            prefix_sum+=nums[i]

            if (prefix_sum -k) in hashmap:
                count+=hashmap[prefix_sum - k]
            
            hashmap[prefix_sum]=hashmap.get(prefix_sum,0)+1
        

        return count
