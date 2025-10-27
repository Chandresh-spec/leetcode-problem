# def cyclicsort(nums):
    # i=0
    # n=len(nums)-1
# 
    # while i <= n :
        # correct_index=nums[i]
        # 
        # if nums[i]<n and nums[i]!= nums[correct_index]:
            # nums[i],nums[correct_index]=nums[correct_index],nums[i]
        # else:
            # i+=1
        # 
    # 
    # 
    # for i in range(len(nums)):
        # if nums[i]!= i :
            # return i
        # 
# 
# 
# nums=[4,5,2,3,0]
# print(cyclicsort(nums))





from typing import List
def findErrorNums(nums: List[int]) -> List[int]:
        i=0
        n=len(nums)

        while i < n :
            correct_index=nums[i]-1

            if nums[i]<= n and nums[i]!= nums[correct_index]:
                nums[i],nums[correct_index]=nums[correct_index],nums[i]
            
            else:
                i+=1

        for i in range(len(nums)):
            if nums[i]!= i+1:
                return [nums[i],i+1]
         

    
    

nums=[1,5,3,2,2,7,6,4,8,9]
print(findErrorNums(nums))