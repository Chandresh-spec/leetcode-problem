# # def binary_search(nums,target):
# #     left=0
# #     right=len(nums)-1

# #     while left < right:
# #         mid=(right+left)//2

# #         if nums[mid]==target:
# #             return nums[mid],True
        

# #         elif target > nums[mid]:
# #             left=mid+1
# #         else:
# #             right=mid-1
    


# # nums=[1,2,3,4,5,6,7,8]
# # target=7
# # print(list(binary_search(nums,target)))
    

# # def lowerBound(nums,target):
# #     lb=0
# #     ub=len(nums)-1
# #     ans=len(nums)

# #     while lb <=ub:
# #         mid=(ub+lb)//2

# #         if nums[mid]>target:
# #             ans=nums[mid]
# #             ub=mid-1
# #         else:
# #             lb=mid+1
        
# #     return ans


# # nums= nums= [3,5,8,9,15,19]
# # x = 9

# # print(lowerBound(nums,x))







# def floorSqrt(n) -> int:
#         lb=1
#         ub=n
#         ans=0

#         while lb <= ub :
#             mid=(ub+lb)//2

#             sqrt=mid*mid


#             if sqrt <= n :
#                 ans=mid
#                 lb=mid+1
            
#             else:
#                 ub=mid-1
            
#         return ans

# n=28
# print(floorSqrt(n))






# def NthRoot(n, m):
       
#     lb=1
#     ub=m
#     ans= -1

#     while lb <= ub :
#         mid=(ub+lb)//2

#         cube=mid*mid*mid
#         if cube==m:
#             return mid

#         if cube < m :
#            lb=mid+1
        
#         else:
#            ub=mid-1
      
#     return ans


# n=3
# m=27
# print(NthRoot(n,m))





# lst=[1,2,3,4]
# hashmap={}
# for i in  range(len(lst)):
#     hashmap[i]=lst[i]

# print(hashmap)





# from typing import List
# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         if len(bloomDay)<m*k:
#             return -1
#         def bloomday(bloomDay,m,k,j):
#             count=0
#             pair=0
#             for i in range(len(bloomDay)):
               
#                 if bloomDay[i]<=j:
#                     count+=1
#                     if count==k:
#                        count=0
#                        pair+=1
                        
#                 else:
#                     count=0
            
#             return  pair >=m
               
            






#         low=min(bloomDay)
#         high=max(bloomDay)

#         while low <= high:
#             mid=(high+low)//2

#             if bloomday(bloomDay,m,k,mid):
#                 high=mid-1
#             else:
#                 low=mid+1
            
#         return low

        



# import math
# class Solution:
#     def smallestDivisor(self, nums: List[int], threshold: int) -> int:


#         def smallest(nums,threshold,j):
#             count=0
#             for i in range(len(nums)):
#                count+=math.ceil(nums[i]/j)
        
#             return count

    



#         lb=1
#         ub=max(nums)

#         while lb <= ub:
#             mid=(ub+lb)//2
   

#             value=smallest(nums,threshold,mid)


#             if value <= threshold:
#                 ub=mid-1
#             else:
#                lb=mid+1
            
#         return lb
        





# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:

#         def check(weights,days,j):
#             count=0
#             total_days=1
#             for i in range(len(weights)):
#                 if count+weights[i]>j:
#                     total_days+=1
#                     count=weights[i]
                    
#                 else:
#                     count+=weights[i]
                   
#             return total_days
            








#         lb=max(weights)
#         ub=sum(weights)

#         while lb <= ub:
#             mid=(ub+lb)//2

#             total_days=check(weights,days,mid)
#             if total_days<=days:
#                 ub=mid-1
              
#             else:
#                   lb=mid+1
                
#         return lb
                
            
       
        



# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
        
#         lb=0
#         ub=len(arr)-1


#         while lb <=ub:
#             mid=(ub+lb)//2


#             missing=arr[mid]-mid
            


#             if missing <= k:
#                 lb=mid+1
#             else:
#                 ub=mid-1
        

#         return lb+k

        


    

         
        



def agressiveCow(nums,k):
    def check(nums,k,j):
        count=1
        start=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-start>=j:
                count+=1
                start=nums[i]
        
        return count>=k



    
    maxi=max(nums)
    mini=min(nums)
    for i in range(1,maxi):
        if not check(nums,k,i):
            return i-1


    
   
    return maxi-nums[0]


nums =  [4, 2, 1, 3, 6]
k=2
nums.sort()
print(agressiveCow(nums,k))



      
            

        

        