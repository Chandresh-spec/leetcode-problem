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


# 
# def find_num(mid,n):
    # num=1
# 
    # for i in range(n):
        # num*=mid
    # 
    # return num
# 
# def NthRoot(n, m):
# 
    # lb=1
    # ub= m
# 
    # while lb <= ub :
        # mid=(ub+lb)//2
        # cal=find_num(mid,n)
# 
        # if cal==m :
        #   return mid
        # 
        # elif cal > m:
        #   ub=mid-1
        # 
        # else:
        #   lb=mid+1
    #   
    # return -1
# 
# 
# n=4
# m=81
# 
# print(NthRoot(n,m))
# 
    # 
# 
# 
# import math
# class Solution:
    # def minEatingSpeed(piles,h) -> int:
# 
        # def find(k,miles):
            # num=0
            # n=len(miles)
            # for i in range(n):
                # num+=math.ceil(miles[i]/k)
            # 
            # return num
# 
        # lb=1
        # ub=max(piles)
        # n=0
        # while lb <= ub :
            # mid=(ub+lb)//2
# 
            # if find(mid,piles) <= h :
                # n=mid
                # ub=mid-1
            # else:
                # lb=mid+1
# 
        # return n
        # 
# 
# 
# import math
# class Solution:
    # def smallestDivisor(self, nums, threshold: int) -> int:
# 
        # def find(nums,mid,threshold):
            # total=0
            # for i in range(len(nums)):
                # total+=math.ceil(nums[i]/mid)
            # 
# 
            # return total
# 
# 
# 
# 
        # lb=1
        # ub=max(nums)
        # while lb <= ub :
            # mid=(ub+lb)//2
# 
            # num=find(nums,mid,threshold)
# 
            # if num <= threshold:
                # ub=mid-1
            # else:
                # lb=mid+1
        # 
        # return lb
# 
# 
# 
# 
        





def floorSqrt(n: int) -> int:
        lb=1
        ub=n
        ans=None

        while lb <= ub :
            mid=(ub+lb)//2


            sqrt=mid*mid

            if sqrt == n:
                 return mid
            if sqrt >= n :
                ub=mid-1
            else:
                ans=mid
                lb=mid+1
        return ans

       

n=28
print(floorSqrt(n))
      

       
from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles,mid,h):
            total=0
            for i in range(len(piles)):
                total+=math.ceil(piles[i]/mid)
            
            return total <= h




        lb=1
        ub=max(piles)
        while lb <= ub :

            mid=(lb+ub)//2

            
            if check(piles,mid,h):
                ub=mid-1
            else:
                lb=mid+1
        
        return lb




class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def find(bloomDay,m,k,mid):
            total=0
            count=0
            for i in range(len(bloomDay)):
                if mid >= bloomDay[i]:
                    count+=1

                    if count==k :
                        total+=1
                        count=0
                    
                else:
                    count=0
                
            return total>= m





        lb=min(bloomDay)
        ub=max(bloomDay)
        ans=-1

        while lb <= ub :
            mid=(ub+lb)//2


            if find(bloomDay,m,k,mid):
                ub=mid-1
                ans=mid
            
            else:
                lb=mid+1
        
        return  ans
            
            
        
        
            

        

        
    