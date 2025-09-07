
def leaders(nums):
        # lst=[]
        # n1=len(nums)
        # for i in range(len(nums)):
        #     current=nums[i]
        #     n=None
        #     for  j in range(i+1,len(nums)):
                
        #         if  current > nums[j]:
        #             n=True
        #         else:
        #             n=False
        #             break

        #     if n :
        #         lst.append(current)   

        # lst.append(nums[n1-1])  
        # return lst
        lst=[]
        gt=float('-inf')
        for i in range(len(nums)-1,-1,-1):
                
            if nums[i] > gt:
                  gt=nums[i]
                  lst.append(gt)
            
        lst.reverse()
        return  lst

                
                



nums =  [1, 2, 5, 3, 1, 2]
print(leaders(nums))