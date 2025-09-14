# Leaders in an Array


0

# 100
# Medium
# 
# Given an integer array nums, return a list of all the leaders in the array.
# 
# 
# 
# A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.
# 
# 
# Examples:
# Input: nums = [1, 2, 5, 3, 1, 2]
# 
# Output: [5, 3, 2]
# 
# Explanation: 2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]
# 
# Input: nums = [-3, 4, 5, 1, -4, -5]
# 
# Output: [5, 1, -4, -5]
# 
# Explanation: -5 is the rightmost element, -4 is the largest element in the index range [4, 5], 1 is the largest element in the index range [3, 5] and 5 is the largest element in the range [2, 5]
# 
# Input: nums = [-3, 4, 5, 1, -30, -10]
def leaders(nums):
        # lst=[]
        # n1=len(nums)
        # for i in range(len(nums)):
        #     current=nums[i]
        #     n=None
        #     for  j in range(i+1,len(nums)):
                
        #         if  current > nums[j]:
        #             n=True
        #         else:
        #             n=False
        #             break

        #     if n :
        #         lst.append(current)   

        # lst.append(nums[n1-1])  
        # return lst
        lst=[]
        gt=float('-inf')
        for i in range(len(nums)-1,-1,-1):
                
            if nums[i] > gt:
                  gt=nums[i]
                  lst.append(gt)
            
        lst.reverse()
        return  lst

                
                



nums =  [1, 2, 5, 3, 1, 2]
print(leaders(nums))