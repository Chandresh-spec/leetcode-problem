#pattern2
#pattern to print only one answer

def subsequence(st,target):
    def helper(index,ds,count):
        if index==len(st):
            if count ==target:
                print(ds)
                return True
            return False
        ds.append(st[index])
        if (helper(index+1,ds,count+st[index])==True):
            return True
        ds.pop()
        if (helper(index+1,ds,count)==True):
            return True
        return False
    
    return helper(0,[],0)


st=[1,2,1]
target=2
print(subsequence(st,target))
