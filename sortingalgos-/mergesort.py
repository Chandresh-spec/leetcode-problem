def insertion_sort(nums):
    for i in range(len(nums)):
        key=nums[i]
        j=i-1

        while j > 0 and key < nums[j]:
            nums[j+1]=nums[j]
            j-=1
        


        nums[j+1]=key

    
    return nums


nums=[1,8,9,6,3,0,2]