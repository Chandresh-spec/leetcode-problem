def sum3(nums):
    lst=set()
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):

                if nums[i]+nums[j]+nums[k]==0:
                    temp=[nums[i],nums[j],nums[k]]

                    temp.sort()
                    lst.add(tuple(temp))

        
   

    newarr=[list(item) for item in lst]

    return newarr




nums=[-1,0,1,2,-1,-4]

print(sum3(nums))



# better


from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        for i in range(len(nums)-1):
            hashmap=set()
            for j in range(i+1,len(nums)):
                third= -(nums[i]+nums[j])
                if third in hashmap:
                        temp=[nums[i],nums[j],third]
                        temp.sort()
                        ans.add(tuple(temp))
                
                hashmap.add(nums[j])
        
        
        items=[list(item) for item in ans]


        return items

                    
        


    
    

        
                        

        






