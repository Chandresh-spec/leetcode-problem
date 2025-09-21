def subarray(nums):
    n=len(nums)
    prefix_sum=[0]*n
    prefix=1

    for i in range(len(nums)):
        prefix_sum[i]=prefix
        prefix*=nums[i]
    

    suffix=1
    for i in range(len(nums)-1,-1,-1):
        prefix_sum[i]*=suffix
        suffix*=nums[i]

    

    return (prefix_sum)
        
        
    

    

    

   



nums=[1,2,3,4]
print(subarray(nums))