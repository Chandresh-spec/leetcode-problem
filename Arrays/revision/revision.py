
# def removeDuplicates(nums) -> int:
#         hashmap={}
#         index=0
#         for i in range(len(nums)):

#             if nums[i] not in hashmap:
#                 nums[index],nums[i]=nums[i],nums[index]
#                 hashmap[nums[index]]=1
#                 index+=1
            

#         return nums


# nums=[0,0,1,1,1,2,2,3,3,4]
# print(removeDuplicates(nums))




def missingNumber(nums) -> int:
        for i in range(len(nums)):
            correct_place=nums[i]

            if correct_place <= len(nums)-1 and i !=nums[correct_place]:
                nums[i],nums[correct_place]=nums[correct_place],nums[i]
        

        return nums
        
        # for i in range(len(nums)):
            # if nums[i]!=i:
                # return i
        # 
        # return i+1
        # 
# 
nums=[9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))