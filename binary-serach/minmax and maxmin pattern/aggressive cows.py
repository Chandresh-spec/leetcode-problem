def aggressive(nums,k):
    lb=0
    ub=max(nums)

    while lb <= ub :
        mid=(ub+lb)//2

        if is_true(mid,nums,k):
            lb=mid+1
        else:
            ub=mid-1
        
    return ub



def is_true(j,nums,k):
    cnt=1
    prev=nums[0]

    for i in range(1,len(nums)):

        if nums[i]-prev >=j:
            cnt+=1
            prev=nums[i]
        
    return cnt >= k



nums =  [10, 1, 2, 7, 5]
k=3
nums.sort()
print(aggressive(nums,k))