
def subarraySum(nums,k) -> int:
        prefix_sum=0
        hashmap={0:1}
        count=0

        for i in range(len(nums)):
            prefix_sum+=nums[i]


            if prefix_sum - k in hashmap:
                count+=hashmap[prefix_sum-k]
            
            hashmap[prefix_sum]=hashmap.get(prefix_sum,0)+1
        

        return count


nums=[1,1,1]
k=2
print(subarraySum(nums,k))