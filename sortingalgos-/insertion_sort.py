def min_max(nums,low,high):
    if low==high:
        return nums[low],nums[low]
    
    elif high-low==1:
        return min(nums[low],nums[high]),max(nums[low],nums[high])
    

    mid=(high+low)//2

    left_min,left_max=min_max(nums,low,mid)
    right_min,right_max=min_max(nums,mid+1,high)

    return min(left_min,right_min),max(left_max,right_max)




nums=[1,8,9,6,3,5,0]
print(min_max(nums,0,len(nums)-1))
