# Find out how many times the array is rotated


# 0

# 100
# Easy

# Given an integer array nums of size n, sorted in ascending order with distinct values. The array has been right rotated an unknown number of times, between 0 and n-1 (including). Determine the number of rotations performed on the array.


# Examples:
# Input : nums = [4, 5, 6, 7, 0, 1, 2, 3]

# Output: 4

# Explanation: The original array should be [0, 1, 2, 3, 4, 5, 6, 7]. So, we can notice that the array has been rotated 4 times.

# Input: nums = [3, 4, 5, 1, 2]

# Output: 3

# Explanation: The original array should be [1, 2, 3, 4, 5]. So, we can notice that the array has been rotated 3 times.




class Solution:
    def findKRotation(self, nums):
        low, high = 0, len(nums) - 1
        ans = 0
        n = len(nums)

        while low <= high:
            mid = (low + high) // 2

            # If current segment is sorted
            if nums[low] <= nums[high]:
                return low   # smallest element index = rotation count

            # Left half is sorted
            if nums[low] <= nums[mid]:
                low = mid + 1

            # Right half is sorted
            else:
                high = mid

        return ans
