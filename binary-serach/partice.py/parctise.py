
def aggresiveCow(nums,k):

      def check(nums,j,k):
            count=1
            cow1=nums[0]
            for i in range(1,len(nums)):

                  if nums[i]-cow1>=j:
                        count+=1
                        cow1=nums[i]
            
            return count
            

            







      ub=max(nums)
      lb=min(nums)

      while lb <= ub :
            mid=(ub+lb)//2


            checkans=check(nums,mid,k)


            if checkans < k:
                  ub=mid-1

            else:
                  lb=mid+1
      

      return ub

                  


            




nums = [10, 1, 2, 7, 5]
nums.sort()
print(aggresiveCow(nums,2))