
# def aggresiveCow(nums,k):

#       def check(nums,j,k):
#             count=1
#             cow1=nums[0]
#             for i in range(1,len(nums)):

#                   if nums[i]-cow1>=j:
#                         count+=1
#                         cow1=nums[i]
            
#             return count
            

            







#       ub=max(nums)
#       lb=min(nums)

#       while lb <= ub :
#             mid=(ub+lb)//2


#             checkans=check(nums,mid,k)


#             if checkans < k:
#                   ub=mid-1

#             else:
#                   lb=mid+1
      

#       return ub

                  


            




# nums = [10, 1, 2, 7, 5]
# nums.sort()
# print(aggresiveCow(nums,2))





# def BookAllocation(nums,k):
# 
# 
      # def check(nums,j,k):
            # count=1
            # sum_of=0
            # for i in range(len(nums)):
            #    if sum_of+nums[i]<=j:
                  # sum_of+=nums[i]
            # 
            #    else:
                  # sum_of=nums[i]
                  # count+=1
            # 
            # return count
            # 
#     
# 
# 
# 
      # lb=max(nums)
      # ub=sum(nums)
# 
      # while lb <= ub :
            # mid=(ub+lb)//2
# 
            # anscheck=check(nums,mid,k)
# 
# 
            # if anscheck > k:
            #      lb=mid+1
            # else:
            #     ub=mid-1
# 
      # return lb
            # 
      # 
      # 
# 
# 
# k=2
# nums =  [12, 34, 67, 90]
# print(BookAllocation(nums,k))






def rowWithMax1s(mat):

        def check(mat,i):
            lb,ub=0,len(mat[i])-1

            while lb <= ub :
                mid=(ub+lb)//2

                if mat[i][mid]==1:
                    ub=mid-1
                else:
                    lb=mid+1
        
            return lb





        n=len(mat)
        m=len(mat[0])
        maxi=0
        index=-1
        for i in range(n):
            ans=check(mat,i)

            count=m-ans
            
            
            if count> maxi:
                maxi=count
                index=i

        return index



mat = [ [0, 0, 1], [0, 1, 1], [0, 1, 1] ]

print(rowWithMax1s(mat))