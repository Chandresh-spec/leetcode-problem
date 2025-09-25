def findErrorNums(nums):
        i=0
        n=len(nums)-1
        while i < n :
            corrected_index=nums[i]-1

            if i<0 and nums[i] != nums[corrected_index]:
                nums[i],nums[corrected_index]=nums[corrected_index],nums[i]
            
            else:
                i+=1

        
        
        for i  in range(len(nums)):
             if i+1 != nums[i]:
                  return [nums[i],i+1]


nums=[1,1]

print(findErrorNums(nums))