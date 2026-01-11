# 
# def shipWithinDays(weights,days):
# 
# 
# 
        # def check(j,weights,days):
            # sum_of=0
            # count=1
# 
            # for i in range(len(weights)):
                # if weights[i]+sum_of <=j:
                    # sum_of+=weights[i]
                # else:
                    # count+=1
                    # sum_of=weights[i]
            # 
            # return count==days
# 
# 
# 
# 
# 
# 
# 
        # lb,ub=min(weights),sum(weights)
        # for i in range(lb,ub):
            # if check(i,weights,days):
                # return i
        # 
        # return -1
# 
# 
# 
# 
# weights = [1,2,3,1,1]
# days = 4
# print(shipWithinDays(weights,days))




# def aggressive_cow(nums,k):
# 
# 
    # def check(j,k,nums):
        # count=1
# 
        # cow=nums[0]
# 
        # for i in range(len(nums)):
            #  if nums[i]-cow>=j:
                #   count+=1
                #   cow=nums[i]
        # 
# 
        # return count
# 
    #  
# 
# 
# 
    # lb=1
    # ub=max(nums)
# 
    # while lb <= ub :
            # mid=(ub+lb)//2
            # val= check(mid,k,nums)
            # if val >=k:
                #  lb=mid+1
            # else:
                #  ub=mid-1
        # 
# 
    # return ub
# 
    #   
        #  
        # 
    # 
# 
# 
# 
# k=2
# nums =  [4, 2, 1, 3, 6]
# nums.sort()
# print(aggressive_cow(nums,k))




def BookAllocation(nums,k):
    def check(j,nums,k):
        sum_of=0
        count=0
        for i in range(len(nums)):
            if sum_of+nums[i]<=j:
                sum_of+=nums[i]
            else:
                count+=1
                sum_of=nums[i]

        
        return





    for i in range(max(nums)+1,sum(nums)):
        if check(i,nums,k):
            return i
        
    
    return -1