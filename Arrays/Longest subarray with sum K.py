def longest_subarray(arr,k):
    prefix_sum=0
    hashmap={0:-1}
    maxi=0

    for index,val in enumerate(arr):
        prefix_sum+=val

        if prefix_sum-k in hashmap:
            maxi=max(maxi,index-hashmap[prefix_sum-k])
        
        hashmap[prefix_sum]=index
    
    return maxi



nums = [10, 5, 2, 7, 1, 9]
k=15

print(longest_subarray(nums,k))
