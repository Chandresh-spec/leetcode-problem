
# Code
# Testcase
# Test Result
# Test Result
# 1004. Max Consecutive Ones III
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length


def max_cons_3(nums,k):
    maxi=0
    st=0
    for i in range(len(nums)):
        if nums[i]==0:
            k-=1  
        if k<0:
                if nums[st]==0:
                    k+=1
                st+=1
         
        maxi=max(maxi,i-st+1)
    
    return maxi


nums = nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(max_cons_3(nums,k))







# def max_cons_3(nums,k):
#     maxi=0
#     st=0
#     for i in range(len(nums)):
#         if nums[i]==0:
#              k-=1
#         if k<0:
#              st+=1
            
#         if k<0:
#              maxi=max(maxi,i-st+1)
    
#     return maxi

# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# print(max_cons_3(nums,k))
    