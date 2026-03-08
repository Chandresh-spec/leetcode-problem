
# def findPages(nums, m):
#         def check(i,nums,m):
#             total=0
#             count=0
#             for j in range(len(nums)):
#                 if total+nums[j]<=i:
#                     total+=nums[j]
                
#                 else:
#                     total=nums[j]
#                     count+=1
                
            
#             if total!=0:
#                  count+=1
            
#             return count


        
#         lb=max(nums)
#         ub=sum(nums)

#         while lb <=ub :
#             mid=(ub+lb)//2

#             total=check(mid,nums,m)

#             if total <=m:
#                  ub=mid-1
#             else:
#                  lb=mid+1
                
            
#         return lb



    
# nums = [25, 46, 28, 49, 24]
# m=4
# print(findPages(nums,m))




# def rowWithMax1s(mat):
#     index=-1
#     maxi=0
#     n,m=len(mat),len(mat[0])
#     for i in range(n):
#         count=0
#         for j in range(m):
#             if mat[i][j]==1:
#                 count+=1
        
#         if count>maxi:
#             index=i
#             maxi=count
        
#     return index





# mat = [ [0, 0, 1], [0, 1, 1], [0, 1, 1] ]
# print(rowWithMax1s(mat))




def findPeakGrid(mat):
        m=len(mat[0])
        n=len(mat)
        for i in range(n):
            for j in range(m):
                left=mat[i][j-1] if j>0 else -1

                right=mat[i][j+1] if j < m-1 else -1

                top=mat[i-1][j] if i>0 else -1

                bottom=mat[i+1][j] if  i < n-1 else -1


                current=mat[i][j]

                if current>left and current>right and current>top and current>bottom:
                    return [i,j]
        
        return False




mat = [[10,20,15],[21,30,14],[7,16,32]]

print(findPeakGrid(mat))