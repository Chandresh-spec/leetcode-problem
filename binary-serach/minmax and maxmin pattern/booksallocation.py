def book_collection(nums,k):
    lb=max(nums)
    ub=sum(nums)

    while lb <= ub :
        mid=(ub+lb)//2

        check=is_true(nums,mid,k)

        if check <=k :
            ub=mid-1
        else:
            lb=mid+1
        
    return ub

def is_true(nums,j,k):
    cnt=1
    total=0
    for i in range(len(nums)):
        if total+nums[i]<j:
            total+=nums[i]
        else:
            cnt+=1
            total=nums[i]
        
    return cnt

nums=[15, 17, 20]
k=2
print(book_collection(nums,k))
            
    