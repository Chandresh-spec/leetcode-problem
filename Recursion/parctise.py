# def subsequence(nums,k):

#     def helper(index,count):
#         if len(nums)==index:
#             if count==k:
#                 return 1
#             return 0
        

#         l=helper(index+1,count+nums[index])
#         r=helper(index+1,count)

#         return l+r
#     return helper(0,0)

        

# nums=[1,2,1]
# k=2
# print(subsequence(nums,k))




# def combinationSum(candidates,target):
#     ans=[]
#     def helper(index,ds,target):
#         if target==0:
#             ans.append(ds[:])
        
#         for i in range(index,len(candidates)):

#             if i>index and candidates[i]==candidates[i-1]:
#                 continue

#             if candidates[i]>target:
#                 break
            
#             ds.append(candidates[i])
#             helper(i+1,ds,target-candidates[i])
#             ds.pop()
        
    
#     helper(0,[],target)
#     return ans
        
       

# candidates = [2,5,2,1,2]
# target = 5
# candidates.sort()
# print(combinationSum(candidates,target))






# def merge(arr,left,mid,right):
#     left_index=left
#     right_index=mid+1
#     nums=[]

#     while left_index<=mid and right_index<=right:
#         if arr[left_index]<=arr[right_index]:
#             nums.append(arr[left_index])
#             left_index+=1
        
#         else:
#             nums.append(arr[right_index])
#             right_index+=1
        
    
#     nums.extend(arr[left_index:])
#     nums.extend(arr[right_index:])


#     for i in range(left, right + 1):
#             arr[i] = nums[i-left]





# def mergesort(arr,left,right):
#     if left>=right:
#         return
    
#     mid=(right+left)//2

#     mergesort(arr,left,mid)
#     mergesort(arr,mid+1,right)
#     return merge(arr,left,mid,right)




# arr=[7, 4, 1, 5, 3]
# print(mergesort(arr,0,len(arr)-1))
# print(arr)




# def partition(arr,low,high):
#     pivot=arr[low]
#     i=low
#     j=high

#     while i <j:
#         while  arr[i]<=pivot and i<high:
#             i+=1
        
#         while arr[j]>=pivot and j>low:
#             j-=1
        

#         if i < j :
#             arr[i],arr[j]=arr[j],arr[i]
        
    
#     arr[j],arr[low]=arr[low],arr[j]

#     return j





# def quicksort(arr,low,high):
#     if (low <high):
#         pi=partition(arr,low,high)

#         quicksort(arr,low,pi-1)
#         quicksort(arr,pi+1,high)



# arr= [7, 4, 1, 5, 3]

# quicksort(arr,0,len(arr)-1)
# print(arr)



# def combination_sum(nums,target):
#     ans=[]
#     def helper(index,ds,target):
#         if index >=len(nums):
#             if target==0:
#                 ans.append(ds[:])   
#             return
        
#         if target>= nums[index]:
#             ds.append(nums[index])
#             helper(index,ds,target-nums[index])
#             ds.pop()
#         helper(index+1,ds,target)
        
    


#     helper(0,[],target)
#     return ans



# nums=[2,3,6,7]
# target=7
# print(combination_sum(nums,target))






# def combination2(nums,target):
#     ans=[]
#     def helper(index,ds,target):
        
#         if index>=len(nums):
#             if target==0:
#                 ans.append(ds[:])
            
#             return
        

#         if target>=nums[index]:
#             ds.append(nums[index])
#             helper(index+1,ds,target-nums[index])
#             ds.pop()
#         helper(index+1,ds,target)


    
#     helper(0,[],target)
#     st=set()
#     for i in ans:
#         i.sort()
#         st.add(tuple(i))
    
    

#     return [ list(item) for item in st]
    
    

# nums=[10,1,2,7,6,1,5]
# target=8
# print(combination2(nums,target))












# def combinationSum2(candidates, target) :
#         ans=[]
#         def helper(index,target,ds):
#             if target==0:
#                 ans.append(ds[:])

#             if index>=len(candidates):
#                 return
            
#             for i in range(index,len(candidates)):
#                 if candidates[i]>target:
#                     break

                
#                 if i >index and candidates[i-1]==candidates[i]:
#                     continue

#                 ds.append(candidates[i])
#                 helper(i+1,target-candidates[i],ds)
#                 ds.pop()
        
#         helper(0,target,[])
#         return ans
    


# candidates = [10,1,2,7,6,1,5]
# target = 8
# candidates.sort()
# print(combinationSum2(candidates,target))




# def combinationSum3(k,n):
#         ans=[]
#         def helper(index,ds,n):
#             if len(ds)==k:
#                 if n==0:
#                     ans.append(ds[:])
                
#                 return 
            
#             for i in range(index,10):

#                 ds.append(i+1)
#                 helper(i+1,ds,n-i)
#                 ds.pop()
        


#         helper(0,[],n)
#         return ans


# k=3
# n=7





def nqueen(n,ans):

    def safe(board,row,col,n):
        j=col
        for i in range(j-1,-1,-1):
            if board[row][i]=='Q':
                return False
        
        
        #upperdiagnal
        i=row
        j=col
        while i>=0 and j >=0:
            if board[i][j]=='Q':
                return False
            i-=1
            j-=1
        

        #lowerdiagnal
        i=row
        j=col
        while i>=0 and i <= n and j >=0 and j <=n:
            if board[i][j]=='Q':
                return False
            
            i+=1
            j-=1
        

        return True
         

    
        

    def helper(col,board):
        if col==n:
            ans.append([''.join(row) for row in board])
            return
        for i in range(n):
            if safe(board,i,col,n-1):
                board[i][col]='Q'
                helper(col+1,board)
                board[i][col]='.'
            
    board=[['.' for i in range(n)]for i in range(n)]
    helper(0,board)
    return ans
    



n=5
ans=[]
print(nqueen(n,ans))
