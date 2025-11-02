def longest(nums,k):
    st=0
    maxi=0
    value=0
    hashmap={}
    for i in range(len(nums)):

        

        if value >k:
            st+=1
            hashmap[nums[st]]=hashmap.get(nums[st],0)-1
        else:
            maxi=max(maxi,i-st+1)
        hashmap[nums[i]]=hashmap.get(nums[i],0)+1
        value=min(hashmap.values())
    return maxi
            

s= "ABAB"
k=2
print(longest(s,k))