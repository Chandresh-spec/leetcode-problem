def binary_search(nums,target):
    left=0
    right=len(nums)-1

    while left < right:
        mid=(right+left)//2

        if nums[mid]==target:
            return nums[mid],True
        

        elif target > nums[mid]:
            left=mid+1
        else:
            right=mid-1
    


nums=[1,2,3,4,5,6,7,8]
target=7
print(list(binary_search(nums,target)))
    