
def subarraySum(nums,k):
        hashmap={0:1}
        sum_of=0
        count=0
        for i in range(len(nums)):
            sum_of+=nums[i]
            if (sum_of-k) in hashmap:

                count+= hashmap[sum_of-k]
            
            hashmap[sum_of]=hashmap.get(sum_of,0)+1
        
        return count

        


nums=[3,1,2,4]
k=6
print(subarraySum(nums,k))
