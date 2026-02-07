
def isTrionic(nums):
        left,mid,right=False,False,False

        for i in range(len(nums)-1):
            if nums[i]<nums[i+1] and mid==False and right==False:
                left=True
            

            elif nums[i]> nums[i+1] and right==False:
                mid=True
            
            elif nums[i]< nums[i+1]  and left and mid:
                right=True
            
            else:
                 return False
        
        return right and left and mid
    

print(isTrionic([8,9,4,6,1]))