def singleNumber(nums) :
        hashmap={}
        for num in range(len(nums)):
                if nums[num] not in hashmap:
                        hashmap[nums[num]]=1
                else:
                        hashmap[nums[num]]+=1
                        
            

        for i,value in hashmap.items():
            if value==1:
                return i
            



nums=[4,1,2,1,2]
print(singleNumber(nums))
        