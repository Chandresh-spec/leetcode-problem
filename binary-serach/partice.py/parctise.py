
def findPages(nums, m):
        def check(i,nums,m):
            total=0
            count=0
            for j in range(len(nums)):
                if total+nums[j]<=i:
                    total+=nums[j]
                
                else:
                    total=nums[j]
                    count+=1
                
            
            if total!=0:
                 count+=1
            
            return count


        
        lb=max(nums)
        ub=sum(nums)

        while lb <=ub :
            mid=(ub+lb)//2

            total=check(mid,nums,m)

            if total <=m:
                 ub=mid-1
            else:
                 lb=mid+1
                
            
        return lb



    
nums = [25, 46, 28, 49, 24]
m=4
print(findPages(nums,m))