def lowerBound(nums, x):
      lb=0
      ub=len(nums)-1
      n=len(nums)
      while lb<=ub:
         mid=(ub+lb)//2

         if nums[mid]>=x:
            n=mid
            ub=mid-1
         else:
            lb=mid+1
      
      return n



nums= [3,5,8,15,19]
x = 9



print(lowerBound(nums,x))