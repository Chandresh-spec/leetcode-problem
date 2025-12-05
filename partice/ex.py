# def selection_sort(nums):
    # for i in range(len(nums)):
        # mini=i
        # for j in range(i+1,len(nums)):
            # if nums[j]< nums[mini]:
                # mini=j
            # 
        # 
        # nums[mini],nums[i]=nums[i],nums[mini]
    # 
    # return nums
# 
# 
# 
# nums=[5,1,2,8,9,6]
# print(selection_sort(nums))
# 
# 
# 
# 
# 
# def find_min_max(nums):
    # if len(nums)==1:
        # return nums[0],nums[0]
    # mid=len(nums)//2
    # left_arr=nums[:mid]
    # right_arr=nums[mid:]
# 
    # left_min,left_max=find_min_max(left_arr)
    # right_min,right_max=find_min_max(right_arr)
# 
    # total_max=max(left_max,right_max)
    # total_min=min(left_min,right_min)
# 
    # return total_min,total_max
# 
# 
# 
# 
# arr = [5, 2, 1, 9, 7, 0]
# print(find_min_max(arr))
# 






# 
# def mergesort(nums):
# 
        # if len(nums)==1:
            # return nums
        # mid=len(nums)//2
        # left_half=nums[:mid]
        # right_half=nums[mid:]
# 
        # left_arr=mergesort(left_half)
        # right_arr=mergesort(right_half)
# 
        # return merge(left_arr,right_arr)
    # 
# 
# def merge(left,right):
    # left_index=0
    # right_index=0
    # arr=[]
# 
    # while left_index<len(left) and right_index<len(right):
        # if left[left_index]<=right[right_index]:
            # arr.append(left[left_index])
            # left_index+=1
        # 
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
# n=int(input("enter the number of element"))
# import random
# import time
# nums=[]
# for i in range(n):
    #  nums.append(random.randint(0,500))
# print(nums)
# print("_"*50) 
# new_arr=mergesort(nums)
# print(new_arr)
# 






def insertion_sort(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1

        while j >=0 and key<nums[j]:
            nums[j+1]=nums[j]
            j-=1
        

        nums[j+1]=key
    
    return nums



nums=[5,4,7,1,0,2]
print(insertion_sort(nums))
