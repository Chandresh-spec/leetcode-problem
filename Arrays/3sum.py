def sum3(nums):
    lst=set()
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):

                if nums[i]+nums[j]+nums[k]==0:
                    temp=[nums[i],nums[j],nums[k]]

                    temp.sort()
                    lst.add(tuple(temp))

        
   

    newarr=[list(item) for item in lst]

    return newarr




nums=[-1,0,1,2,-1,-4]

print(sum3(nums))