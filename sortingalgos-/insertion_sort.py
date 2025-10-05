def insertion_sort(arr): 
    for i in range(1, len(arr)): 
        key=nums[i]
        j=i-1

        while j>=0 and nums[j] >key:
            nums[j+1]=nums[j]
            j-=1
        
        nums[j+1]=key
       
    
    return nums


nums=[5,0,3,4,5,8]
print(insertion_sort(nums))