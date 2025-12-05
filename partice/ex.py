def selection_sort(nums):
    for i in range(len(nums)):
        mini=i
        for j in range(i+1,len(nums)):
            if nums[j]< nums[mini]:
                mini=j
            
        
        nums[mini],nums[i]=nums[i],nums[mini]
    
    return nums



nums=[5,1,2,8,9,6]
print(selection_sort(nums))





def find_min_max(nums):
    if len(nums)==1:
        return nums[0],nums[0]
    mid=len(nums)//2
    left_arr=nums[:mid]
    right_arr=nums[mid:]

    left_min,left_max=find_min_max(left_arr)
    right_min,right_max=find_min_max(right_arr)

    total_max=max(left_max,right_max)
    total_min=min(left_min,right_min)

    return total_min,total_max




arr = [5, 2, 1, 9, 7, 0]
print(find_min_max(arr))