# parameterised Recursion

# def helper(n,count):
#     if n==1:
#         print(count+1)
#         return

    
#     helper(n-1,count+n)


# helper(5,0)

# functional_recursion


# def helper(n):
#     if n ==1:
#         return 1
    
#     return n+helper(n-1)


# print(helper(5))



def subsequence(nums,k):
    ans=[]
    def helper(index,count):
        if index>=len(nums):
            if count==k:
                return 1
            return 0

    
        
        l=helper(index+1,count+nums[index])
        
        r=helper(index+1,count)

        return l+r
            

    return helper(0,0)
    


nums=[1,2,1]
print(subsequence(nums,2))
            