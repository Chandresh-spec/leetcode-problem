def maxSlidingWindow(nums,k):
    arr=[]
    for i in range(len(nums)-k+1):
        maxi=0
        for j in range(i,i+k):
            maxi=max(maxi,nums[j])
        
        arr.append(maxi)
    
    return arr




nums=[1]
k = 1
print(maxSlidingWindow(nums,k))