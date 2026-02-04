def subsequence(nums,k):
    ans=[]
    def helper(index,count):
        if len(nums)==index:
            if count==k:
                return 1
            return 0
        

        l=helper(index+1,count+nums[index])
        r=helper(index+1,count)

        return l+r
    return helper(0,0)

        

nums=[1,2,1]
k=2
print(subsequence(nums,k))