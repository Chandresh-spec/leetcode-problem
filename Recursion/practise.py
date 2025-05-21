def subset(num):
    ds=[]
    def helper(index,count):
        
        if index==len(num):
            ds.append(count)
            return 
        
        helper(index+1,count+num[index])
        helper(index+1,count)

    helper(0,0)
    return ds

num=[5, 2, 1]
print(subset(num))

def combination_sum(candidates,target):
    ans=[]
    def helper(index,ds,target):
        if len(candidates)==index:
            if target==0:
                ans.append(ds[index])
            return
        
        if target>candidates[index]:
            ds.append(candidates[index])
            helper(index,ds,target-candidates[index])
            ds.pop()
        helper(index+1,ds,target-candidates[index])
    
    helper(0,[],0)
    return ans


    

