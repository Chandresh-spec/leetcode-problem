def subarray(nums):
    total=0
    for i in range(len(nums)):
        mini=0
        maxi=0
        for j in range(i+1,len(nums)):
            mini=min(nums[i:j+1])
            maxi=max(nums[i:j+1])

            total+=maxi-mini

        
    return total




nums = [4,-2,-3,4,1]
print(subarray(nums))