
# def subarraySum(nums,k) -> int:
#         prefix_sum=0
#         hashmap={0:1}
#         count=0

#         for i in range(len(nums)):
#             prefix_sum+=nums[i]


#             if prefix_sum - k in hashmap:
#                 count+=hashmap[prefix_sum-k]
            
#             hashmap[prefix_sum]=hashmap.get(prefix_sum,0)+1
        

#         return count


# nums=[1,1,1]
# k=2
# print(subarraySum(nums,k))



# continous subarray

from typing import List
# def checkSubarraySum(nums: List[int], k: int) -> bool:
        # hashmap={0:-1}
        # sum_of=0
# 
        # for i in range(len(nums)):
            # sum_of+=nums[i]
            # val=sum_of%k
# 
            # if val in hashmap:
                # if i-hashmap[val] >= 1 :
                    # return True
                # 
            # else:
                #  hashmap[val]=i
        # 
        # return False
# 
# 
# nums=[5,0,0,0]
# k=3
# print(checkSubarraySum(nums,k))





# 
# class Solution:
    # def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # sum_of=0
        # count=0
        # hashmap={0:1}
        # for num in nums:
            # sum_of+=num
# 
            # val=sum_of%k
# 
            # if val in hashmap:
                # count+=hashmap[val]
            # 
            # hashmap[val]=hashmap.get(val,0)+1
        # 
# 
        # return count
    # 
# 
# 
# 
# class Solution:
    # def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # hashmap={0:1}
        # count=0
        # val=0
        # for num in nums:
# 
            # val+=num
# 
            # if val-goal in hashmap:
                # count+=hashmap[val-goal]
            # 
            # hashmap[val]=hashmap.get(val,0)+1
        # 
# 
        # return count
    # 






# def numberOfSubarrays(nums,k) -> int:
        # 
        # total=0
        # for i in range(len(nums)):
            # num_count=0
            # 
            # for j in range(i,len(nums)):
                # if nums[j]%2==1:
                    # num_count+=1
                # 
                # if num_count==k:
                    # total+=1
                # 
            # 
        # return total
# 
# 
# 
# nums=[2,2,2,1,2,2,1,2,2,2]
# k=2
# print(numberOfSubarrays(nums,k))







class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        hashmap={0:1}
        total=0
        count=0
        for num in nums:
            if num%2==1:
                count+=1
            

            if count-k in hashmap:
                total+=hashmap[count-k]
            
            hashmap[count]=hashmap.get(count,0)+1
        

        return total



       