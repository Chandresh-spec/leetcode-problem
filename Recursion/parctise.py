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



def combination_sum(nums,target):
    ans=[]
    def helper(index,ds,target):
        if index >=len(nums):
            if target==0:
                ans.append(ds[:])   
            return
        
        if target>= nums[index]:
            ds.append(nums[index])
            helper(index,ds,target-nums[index])
            ds.pop()
        helper(index+1,ds,target)
        
    


    helper(0,[],target)
    return ans



nums=[2,3,6,7]
target=7
print(combination_sum(nums,target))