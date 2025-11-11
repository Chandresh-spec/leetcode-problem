# def binary_search(nums,target):
#     left=0
#     right=len(nums)-1

#     while left < right:
#         mid=(right+left)//2

#         if nums[mid]==target:
#             return nums[mid],True
        

#         elif target > nums[mid]:
#             left=mid+1
#         else:
#             right=mid-1
    


# nums=[1,2,3,4,5,6,7,8]
# target=7
# print(list(binary_search(nums,target)))
    

# def lowerBound(nums,target):
#     lb=0
#     ub=len(nums)-1
#     ans=len(nums)

#     while lb <=ub:
#         mid=(ub+lb)//2

#         if nums[mid]>target:
#             ans=nums[mid]
#             ub=mid-1
#         else:
#             lb=mid+1
        
#     return ans


# nums= nums= [3,5,8,9,15,19]
# x = 9

# print(lowerBound(nums,x))







def floorSqrt(n) -> int:
        lb=1
        ub=n
        ans=0

        while lb <= ub :
            mid=(ub+lb)//2

            sqrt=mid*mid


            if sqrt <= n :
                ans=mid
                lb=mid+1
            
            else:
                ub=mid-1
            
        return ans

n=28
print(floorSqrt(n))






def NthRoot(n, m):
       
    lb=1
    ub=m
    ans= -1

    while lb <= ub :
        mid=(ub+lb)//2

        cube=mid*mid*mid
        if cube==m:
            return mid

        if cube < m :
           lb=mid+1
        
        else:
           ub=mid-1
      
    return ans


n=3
m=27
print(NthRoot(n,m))





lst=[1,2,3,4]
hashmap={}
for i in  range(len(lst)):
    hashmap[i]=lst[i]

print(hashmap)