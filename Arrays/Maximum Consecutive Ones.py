# 485. Max Consecutive Ones
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.




def longest_subarray(nums,k):
    maxi=0
    for i in range(len(nums)):
        count=1
        cal=nums[i]
        for j in range(1,len(nums)):
            if cal == k:
                maxi=max(count,maxi)
            
            elif cal <k:
                cal=cal+nums[j]
                count+=1
            else:
                break
        
    return maxi

nums = [-1, 1, 1]
k=1
print(longest_subarray(nums,k))
            

