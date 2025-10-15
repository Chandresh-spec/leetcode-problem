def BubbleSort(nums):

    n=len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]> nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

        
    return nums



arr=[1,8,9,6,7,5,3,2]
print(BubbleSort(arr))