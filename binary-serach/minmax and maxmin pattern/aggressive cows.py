def aggressive(nums,k):

    maxi=max(nums)

    for i in range(1,maxi+1):
        if is_true(i,nums,k):
            continue
        else:
            break
    
    return i-1



def is_true(j,nums,k):
    cnt=1
    prev=nums[0]

    for i in range(1,len(nums)):

        if nums[i]-prev >=j:
            cnt+=1
            prev=nums[i]
        
    return cnt >= k



nums =   [10, 1, 2, 7, 5]
k=3
nums.sort()
print(aggressive(nums,k))