def mergesort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left_half=mergesort(left_arr)
    right_half=mergesort(right_arr)
    return merge(left_half,right_half)

def merge(left,right):
    temp=[]
    left_index=0
    right_index=0
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            temp.append(left[left_index])
            left_index+=1
        else:
            temp.append(right[right_index])
            right_index+=1
    temp.extend(left[left_index:])
    temp.extend(right[right_index:])
    return temp



arr=[3,5,2,7,8,1,9]
print("before sorting:",arr)
arr=mergesort(arr)
print("after sorting:",arr)