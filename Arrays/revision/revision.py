# def largest_element(nums):
#     # largest_element=float('-inf')
#     # for i in nums:
#         # if i > largest_element:
#             # largest_element=i
#         # 
#     # 
#     # return largest_element

#     nums.sort(reverse=False)

#     return nums
    




# nums=[1,8,9,6,3,1]
# print(largest_element(nums))

# #o(n)







# # if if the sorted array()
# from typing import List

# # class Solution:
#     def check(self, nums: List[int]) -> bool:
#         count=0
#         n=len(nums)

#         for i in range(n):
#             index=(i+1)%n

#             if nums[i]> nums[index]:
#                 count+=1
            
#         return count==1 or count==0









# def remove_duplicate(nums):
    # j=0
    # for i in range(1,len(nums)):
        # if nums[i]>nums[j]:
            # j+=1
            # nums[i],nums[j]=nums[j],nums[i]
        # 
    # return j+1
            # 
# 
# 
# nums = [1,1,2]
# print(remove_duplicate(nums))
# 
# 


# rotate array


def rotatearray(nums,k):
    def rotate(nums,st,end):
        
        while st <= end :
            nums[st],nums[end]=nums[end],nums[st]
            st+=1
            end-=1
        
        return nums
    

    rotate(nums,0,len(nums)-1)

    rotate(nums,0,k-1)

    rotate(nums,k,len(nums)-1)


    return nums

nums=[-1,-100,3,99]
k=2
print(rotatearray(nums,k))




from typing import List
def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):

            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            
        return nums

       

        


