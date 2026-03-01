# def subarray(nums):
#     total=0
#     for i in range(len(nums)):
#         mini=0
#         maxi=0
#         for j in range(i+1,len(nums)):
#             mini=min(nums[i:j+1])
#             maxi=max(nums[i:j+1])

#             total+=maxi-mini

        
#     return total




# nums = [4,-2,-3,4,1]
# print(subarray(nums))


def findnse(nums):
        n=len(nums)
        nse=[n]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and nums[i]<nums[stack[-1]]:
                  stack.pop()
            
            if stack:
                  nse[i]=stack[-1]
                
            stack.append(i)
                
        return nse


def findpse(nums):
        n=len(nums)
        stack=[]
        pse=[-1]*n
        for i in range(n):
            while stack  and nums[i]<nums[stack[-1]]:
                  stack.pop()
            
            if stack:
                  pse[i]=stack[-1]
                
            
            stack.append(i)
        
        return pse

def subarrayMinimus(nums):
        count=0
        nse=findnse(nums)
        pse=findpse(nums)
        for i in range(len(nums)):
            left=i-pse[i]
            right=nse[i]-i

            total=left*right
            count+=total*nums[i]
        
        return count
        
    
            
        

    
nums=[11,81,94,43,3]
print(subarrayMinimus(nums))
            