import math
from typing import List

def smallestDivisor(nums: List[int], threshold: int) -> int:

        low=1
        high=max(nums)
        ans=0

        def f(mid,nums):
            total=0
            for i in nums:
                total+=math.ceil(i/mid)
            return total

        while low <= high:
            mid=(high+low)//2
            cal=f(mid,nums)
            if cal<= threshold:
                high=mid-1
                ans=mid
            else:
                low=mid+1
            
        return ans

nums = [44,22,33,11,1]
threshold = 5
print(smallestDivisor(nums,threshold))


        
        