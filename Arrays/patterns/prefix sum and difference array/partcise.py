
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






class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_of=0
        count=0
        hashmap={0:1}
        for num in nums:
            sum_of+=num

            val=sum_of%k

            if val in hashmap:
                count+=hashmap[val]
            
            hashmap[val]=hashmap.get(val,0)+1
        

        return count
       