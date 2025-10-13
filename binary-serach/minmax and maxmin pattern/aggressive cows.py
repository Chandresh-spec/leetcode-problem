
def aggressiveCows(nums, k):


        def is_count(nums,i,k):
            cnt=1
            prev=0
            for j in range(len(nums)):
                if nums[j]-prev <=i :
                     cnt+=1
                     prev=nums[j]
                
            return cnt>=k
        n=max(nums)

        for i in range(1,n):

            if is_count(nums,i,k):
                 return  i
        


        return  -1

            
            
            


nums =  [4, 2, 1, 3, 6]
k=2
nums.sort()
print(aggressiveCows(nums,k))
        