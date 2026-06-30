def aggressiveCows(nums, k):

        def check(i,nums,k):
            cow=nums[0]
            count=1
            for j in range(1,len(nums)):
                if abs(cow-nums[j])>=i:
                    count+=1
                    cow=nums[j]
            

            return count

        nums.sort()

        lb=1
        ub=max(nums)


        while lb <= ub :
            mid=(ub+lb)//2


            ans=check(mid,nums,k)

            if ans >=k:
                lb=mid+1
            
            else:
                ub=mid-1
        

        return ub
        






k = 2
nums = [4, 2, 1, 3, 6]
print(aggressiveCows(nums,k))









