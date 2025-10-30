def permutation(nums):
    maxi= -1
    index=-1
    for i in range(len(nums)-2,-1,-1):

        if nums[i]<nums[maxi]:
            index=i
            break
            
        else:
            if nums[i]>nums[maxi]:
                maxi=i

    small=0
    for i in range(i+1,len(nums)):
        if nums[i]>nums[index] and nums[i]<nums[]

nums=[3,2,1]
print(permutation(nums))
