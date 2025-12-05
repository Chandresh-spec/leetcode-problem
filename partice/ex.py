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