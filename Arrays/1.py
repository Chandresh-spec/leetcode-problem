def findlargest(nums):
    n=0
    for i in range(len(nums)):
        if nums[i]>n:
            n=nums[i]
        
    return n





nums=[1,8,6,3,9,4]
print(findlargest(nums))
