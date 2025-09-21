def pivot_index(nums):
    sum_of=sum(nums)
    left_sum=0
    for i in range(len(nums)):
        
        sum_of -= nums[i]
        if sum_of== left_sum:
            return i
        
        left_sum+=nums[i]

    return -1



nums =[2,1,-1]
print(pivot_index(nums))