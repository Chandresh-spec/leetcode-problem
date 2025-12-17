# def helper(cnt):
#     if cnt==4:
#         return
    

#     print(cnt)
#     helper(cnt+1)



# cnt=0
# helper(cnt)




# def target_sum(nums,target):
    # def f(count,index):
        # 
        # if index==len(nums):
            # if count==target:
                # return True
            # return False
            # 
            # return
        # 
        # if f(count+nums[index],index+1)==True:
            # return True
        # if f(count,index+1)==True:
            # return True
        # 
        # return False
# 
    # 
    # return f(0,0)
    # 
# 
# nums=[4, 2, 10, 5, 1, 3]
# target=99
# print(target_sum(nums,target))
# 
# 
# 



def helper(nums,target):
    def f(index,count):
        if index == len(nums):
            if count==target:
                return 1
            return 0
        
        return f(index+1,count+nums[index]) +f(index+1,count)


    
    return f(0,0)


nums=[1,2,3]
print(helper(nums,3))





    

