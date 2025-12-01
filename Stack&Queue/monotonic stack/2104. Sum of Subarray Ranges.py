
from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total=0
        for i in range(len(nums)):
            smallest=float('inf')
            greater=float('-inf')
            for j in range(i,len(nums)):
                smallest=min(smallest,nums[j])
                greater=max(greater,nums[j])

                total+=greater-smallest
            
        return total