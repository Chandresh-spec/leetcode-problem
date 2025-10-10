# def floorandciel(nums,target):
#     lb=0
#     ub=len(nums)-1
#     floor= -1
#     ciel =len(nums)

#     while lb <= ub :
#         mid=(ub+lb)//2
        

#         if nums[mid]>= target:
#             ciel=mid
#             ub=mid-1
#         else:
#             floor=mid
#             lb=mid+1
        
    
#     if  ciel < len(nums) and nums[ciel]==target:
#         return [target,target]
    
#     if floor == -1 :
#         return [floor,nums[ciel]]
    
#     return [nums[floor],nums[ciel]]

# nums = [2, 4, 6, 8, 10, 12, 14]
# x= 1
# print(floorandciel(nums,x))
    





# def floorSqrt(n: int) -> int:
        # lb=1
        # ub=n
        # sq=None
# 
        # while lb <= ub :
            # mid=(ub+lb)//2
# 
            # square_root=mid*mid
# 
            # if square_root <= n :
                # sq=mid
                # lb= mid+1
            # else:
                # ub=mid-1
            # 
            # 
        # return sq
    # 
# 
# n=36
# 
# print(floorSqrt(n))



def find_num(mid,n):
    num=1

    for i in range(n):
        num*=mid
    
    return num

def NthRoot(n, m):

    lb=1
    ub= m

    while lb <= ub :
        mid=(ub+lb)//2
        cal=find_num(mid,n)

        if cal==m :
          return mid
        
        elif cal > m:
          ub=mid-1
        
        else:
          lb=mid+1
      
    return -1


n=4
m=81

print(NthRoot(n,m))

    


import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def find(k,miles):
            num=0
            n=len(miles)
            for i in range(n):
                num+=math.ceil(miles[i]/k)
            
            return num

        lb=1
        ub=max(piles)
        n=0
        while lb <= ub :
            mid=(ub+lb)//2

            if find(mid,piles) <= h :
                n=mid
                ub=mid-1
            else:
                lb=mid+1

        return n
        


        





      
    
      

      