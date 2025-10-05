def floorandciel(nums,target):
    lb=0
    ub=len(nums)-1
    floor= -1
    ciel =len(nums)

    while lb <= ub :
        mid=(ub+lb)//2
        

        if nums[mid]>= target:
            ciel=mid
            ub=mid-1
        else:
            floor=mid
            lb=mid+1
        
    
    if  ciel < len(nums) and nums[ciel]==target:
        return [target,target]
    
    if floor == -1 :
        return [floor,nums[ciel]]
    
    return [nums[floor],nums[ciel]]

nums = [2, 4, 6, 8, 10, 12, 14]
x= 1
print(floorandciel(nums,x))
        