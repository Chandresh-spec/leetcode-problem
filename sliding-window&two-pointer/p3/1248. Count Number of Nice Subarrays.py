
def numberOfSubarrays(nums, k) -> int:
        maxi=0
        st=0
        odd=0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                if nums[st] %2==1:
                     odd -= 1
                st+=1
            
            while  odd > k:
                st+=1
            
            maxi+= i-st+1
         
          
        return maxi
    # return numberOfSubarrays


nums=[1,1,2,1,1]
k=3
print(numberOfSubarrays(nums,k))