def substring(nums):
    count=0
    for i in range(len(nums)):
        hashmap={'a':0,'b':0,'c':0}
        for j in range(i,len(nums)):
            hashmap[nums[j]]=1

            min_val=min(hashmap.values())

            if min_val==1:
                count+=1
            
        
    return count




nums="abc"
print(substring(nums))