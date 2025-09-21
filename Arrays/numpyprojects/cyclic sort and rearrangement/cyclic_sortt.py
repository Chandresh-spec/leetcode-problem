def cyclic_sort(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct_index = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    # return nums
    
    for i in range(len(nums)):
        if i+1 !=  nums[i]:
            return i+1
    
    return n

nums = [1,2,0]
print(cyclic_sort(nums))  # [1, -1, 3, 4]
