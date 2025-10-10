def find_min_max(nums):

    if len(nums)==1:
        return [nums[0],nums[0]]
    
    if len(nums)==2:
        return [min(nums),max(nums)]
    
    mid=len(nums)//2
    left_arr=nums[:mid]
    right_arr=nums[mid:]

    l_min,l_max=find_min_max(left_arr)
    b_min,b_max=find_min_max(right_arr)

    return [max(l_min,b_min),min(l_max,b_max)]


nums=[1,89,6,32,4]

print(find_min_max(nums))
    