from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        

        def binary_sum(nums,goal):
            if goal < 0:
                return 0
            count=0
            sum_of=0
            st=0
            for i in range(len(nums)):
                count+=nums[i]

                while count>goal:
                    count-=nums[st]
                    st+=1
                
                sum_of+=i-st+1
            
            return sum_of
        

        return binary_sum(nums,goal)-binary_sum(nums,goal-1)

        