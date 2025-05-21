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