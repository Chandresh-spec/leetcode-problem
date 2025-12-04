# def min_max(nums,low,high):
    # if low==high:
        # return nums[low],nums[low]
    # 
    # elif high-low==1:
        # return min(nums[low],nums[high]),max(nums[low],nums[high])
    # 
# 
    # mid=(high+low)//2
# 
    # left_min,left_max=min_max(nums,low,mid)
    # right_min,right_max=min_max(nums,mid+1,high)
# 
    # return min(left_min,right_min),max(left_max,right_max)
# 
# 
# 
# 
# nums=[1,8,9,6,3,5,0]
# print(min_max(nums,0,len(nums)-1))
# 


# 
# def insertion_sort(nums):
    # for i in range(1,len(nums)):
        # key=nums[i]
        # j=i-1
# 
        # while j >=0 and key < nums[j]:
            # nums[j+1]=nums[j]
            # j-=1
        # 
# 
        # nums[j+1]=key
    # 
# 
    # return nums
# 
# 
# 
# nums=[1,8,9,6,3,5,0]
# print(insertion_sort(nums))



def selectionSort(nums):
    for i in range(len(nums)):
        mini=i
        for j in range(i,len(nums)):
            if nums[j]<nums[mini]:
                mini=j
            
        nums[i],nums[mini]=nums[mini],nums[i]
    
    return nums



n=int(input("enter the number of element u want to insert:"))
nums=[]
for i in range(n):
    nums.append(int(input(f"enter {i+1}th element:")))

print("after sorting")
print(selectionSort(nums))



