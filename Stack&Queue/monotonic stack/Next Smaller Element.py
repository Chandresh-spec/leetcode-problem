def NSE(nums):
    n=len(nums)
    arr=[-1]*n
    stack=[]
    for i in range(len(nums)-1,-1,-1):
        while stack and stack[-1]>=nums[i]:
            stack.pop()
        

        if stack:
            arr[i]=stack[-1]
        stack.append(nums[i])
    

    return arr




arr = [4, 8, 5, 2, 25]
print(NSE(arr))
