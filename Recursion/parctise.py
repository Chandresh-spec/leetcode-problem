# def helper(cnt):
#     if cnt==4:
#         return
    

#     print(cnt)
#     helper(cnt+1)



# cnt=0
# helper(cnt)




# def target_sum(nums,target):
    # def f(count,index):
        # 
        # if index==len(nums):
            # if count==target:
                # return True
            # return False
            # 
            # return
        # 
        # if f(count+nums[index],index+1)==True:
            # return True
        # if f(count,index+1)==True:
            # return True
        # 
        # return False
# 
    # 
    # return f(0,0)
    # 
# 
# nums=[4, 2, 10, 5, 1, 3]
# target=99
# print(target_sum(nums,target))
# 
# 
# 



# def helper(nums,target):
    # def f(index,count):
        # if index == len(nums):
            # if count==target:
                # return 1
            # return 0
        # 
        # return f(index+1,count+nums[index]) +f(index+1,count)
# 
# 
    # 
    # return f(0,0)
# 
# 
# nums=[1,2,3]
# print(helper(nums,3))





    

# def mergesort(nums):
    # if len(nums)==1:
        # return nums
    # 
    # mid=len(nums)//2
    # left_arr=nums[:mid]
    # right_arr=nums[mid:]
# 
    # left_half=mergesort(left_arr)
    # right_half=mergesort(right_arr)
    # return merge(left_half,right_half)
# 
# 
# 
# def merge(left,right):
    # left_index=0
    # right_index=0
    # arr=[]
    # while left_index < len(left) and right_index < len(right):
        # if left[left_index] <= right[right_index]:
            # arr.append(left[left_index])
            # left_index+=1
        # else:
            # arr.append(right[right_index])
            # right_index+=1
        # 
    # 
    # arr.extend(left[left_index:])
    # arr.extend(right[right_index:])
# 
    # return arr
# 
# 
# 
# 
# nums=[1,8,9,6,3,5]
# print(mergesort(nums))
# 
# 




# QuickSort()



# def quicksort(arr,lb,ub):
    # if lb < ub :
        # pi=partition(arr,lb,ub)
# 
        # quicksort(arr,lb,pi-1)
        # quicksort(arr,pi+1,ub)
# 
# 
# 
# def partition(arr,lb,ub):
    # pivot=lb
    # i=lb+1
    # j=ub
# 
    # while i < j :
        # while arr[i]<=arr[pivot] and i < j :
            # i+=1
        # 
        # while arr[j]>= arr[pivot] and i < j:
# 
            # j-=1
        # arr[i],arr[j]=arr[j],arr[i]
    # 
    # arr[i-1],arr[pivot]=arr[pivot],arr[i-1]
# 
    # return i-1
# 
# 
# 
# 
# nums=[1,8,9,6,3,5]
# print(quicksort(nums,0,len(nums)-1))
# print(nums)
# 
# 




# def combination_sum(candidate,target):
    # ans=set()
    # def helper(index,ds,target):
        # if len(candidate)==index:
        #    if target == 0:
            #    ans.add(tuple(ds[:]))
        #    return
        # 
        # if candidate[index]<=target:
        # 
            # ds.append(candidate[index])
            # helper(index,ds,target-candidate[index])
            # ds.pop()
        # helper(index+1,ds,target)
    # 
# 
# 
# 
# 
    # helper(0,[],target)
    # return [list(item) for item in ans]
# 
# 
# 
# 
# candidates = [2,3,6,7]
# target = 7
# print(combination_sum(candidates,target))




# 
# def combination2(nums,target):
    # ans=[]
    # def helper(index,ds,target):
# 
        # if target==0:
            # ans.append(ds[:])
        # 
# 
        # for i in range(index,len(nums)):
            # if i> index and nums[i]==nums[i-1]:
                # continue
# 
            # if nums[i]>target:
                # break
# 
            # ds.append(nums[i])
            # helper(i+1,ds,target-nums[i])
            # ds.pop()
        # 
    # 
    # helper(0,[],target)
    # return ans
# 
# 
# 
# nums=[1,1,1,2,2]
# target=4
# print(combination2(nums,target))




def subset(nums):
    ans=[]
    def helper(index,count):
        if index==len(nums):
            ans.append(count)
            return
        helper(index+1,count+nums[index])
        helper(index+1,count)
    helper(0,0)
    return ans
nums = [2, 3]
print(subset(nums))


