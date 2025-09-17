# 229. Majority Element II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# 
#  
# 
# Example 1:
# 
# Input: nums = [3,2,3]
# Output: [3]
# Example 2:
# 
# Input: nums = [1]
# Output: [1]
# Example 3:
# 
# Input: nums = [1,2]
# Output: [1,2]
#  
# 
# Constraints:
# 
# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
#  
# 
# Follow up: Could you solve the problem in linear time and in O(1) space?
def majorityElement(nums):
        cnt1,cnt2=0,0
        maj1,maj2=float('-inf'),float('-inf')

        for i in nums:

            if cnt1==0 and i!=maj2:
                maj1=i
                cnt1=1
            elif cnt2==0 and i!=maj1:
                maj2=i
                cnt2=1
            
            elif maj1==i:
                cnt1+=1
            
            elif maj2==i:
                cnt2+=1
            
            else:
                cnt1-=1
                cnt2-=1
        
        count1=0
        count2=0

        for num in nums:
            if num==maj1:
                count1+=1
            if num == maj2:
                count2+=1
        

        lst=[]

        if count1>len(nums)//3:
            lst.append(maj1)
        

        if count2>len(nums)//3:
            lst.append(maj2)
        
        return lst
        

        
