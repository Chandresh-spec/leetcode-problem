def longest_subarray(arr,k):
    maxi=0
    for i in range(len(arr)):
        sm=arr[i]
        count=1
        for j in range(i+1,len(arr)):
            sm+=arr[j]
            if sm==k:
                maxi=max(maxi,count)
            if sm>k:
                break
            else:
                count+=1
        maxi=max(maxi,count)
    
    if maxi==0:
        return -1
    else:
        return maxi

nums = [-3, 2, 1]
k=6
print(longest_subarray(nums,k))
