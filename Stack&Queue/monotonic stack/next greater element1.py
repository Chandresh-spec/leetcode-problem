def nextGreater(nums1,nums2):
    dict1={}
    stack=[]

    for i in range(len(nums2)-1,-1,-1):
        while stack and nums2[i]>stack[-1]:
            stack.pop()
        
        if not stack:
            dict1[nums2[i]]=-1
        else:
           dict1[nums2[i]]=stack[-1]

        stack.append(nums2[i])
    
    res=[]
    for i in range(len(nums1)):
        res.append(dict1[nums1[i]])
    
    return res
    

nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreater(nums1,nums2))






