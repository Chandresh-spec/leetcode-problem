def MinimalRemoval(nums,k):
    nums.sort()
    for i in range(len(nums)-1,-1,-1):

        for j in range(len(nums)):

            if nums[i]<= nums[j]*k:
                ans=  len(nums)-(i-j+1)
                return ans
        
    

    return 0





nums = [1,34,23]
k = 2

print(MinimalRemoval(nums,k))