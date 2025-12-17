# def helper(cnt):
#     if cnt==4:
#         return
    

#     print(cnt)
#     helper(cnt+1)



# cnt=0
# helper(cnt)




def target_sum(nums,target):
    ans=0
    def f(count,index):
        nonlocal ans
        if index==len(nums):
            if count==target:
                ans+=1
            
            return
        
        f(count+nums[index],index+1)
        f(count,index+1)

    
    f(0,0)
    print(ans)

nums=[4, 2, 10, 5, 1, 3]
target=5
target_sum(nums,target)
    

