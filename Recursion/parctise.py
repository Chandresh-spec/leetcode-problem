# def subsequence(nums,k):

#     def helper(index,count):
#         if len(nums)==index:
#             if count==k:
#                 return 1
#             return 0
        

#         l=helper(index+1,count+nums[index])
#         r=helper(index+1,count)

#         return l+r
#     return helper(0,0)

        

# nums=[1,2,1]
# k=2
# print(subsequence(nums,k))




def combinationSum(candidates,target):
    ans=[]
    def helper(index,ds,target):
        if target==0:
            ans.append(ds[:])
        
        for i in range(index,len(candidates)):

            if i>index and candidates[i]==candidates[i-1]:
                continue

            if candidates[i]>target:
                break
            
            ds.append(candidates[i])
            helper(i+1,ds,target-candidates[i])
            ds.pop()
        
    
    helper(0,[],target)
    return ans
        
       

candidates = [2,5,2,1,2]
target = 5
candidates.sort()
print(combinationSum(candidates,target))





