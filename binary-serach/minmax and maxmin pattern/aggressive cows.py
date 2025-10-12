def  aggressivecow(nums,k):

    lb=1
    ub=max(nums)
    while lb <= ub :
        mid=(ub+lb)//2

        if is_cow(nums,mid,k):
            lb=mid+1
        else:
            ub=mid-1
        
    return ub
    
    



def is_cow(nums,j,k):
    last=nums[0]
    cnt=1
    for i in range(1,len(nums)):
        if nums[i]- last >= j :
            cnt+=1
            last=nums[i]

            if cnt >= k :
                return True
    return False
    
    
   


nums = [10, 1, 2, 7, 5]

nums.sort()
k=3
print(aggressivecow(nums,k))