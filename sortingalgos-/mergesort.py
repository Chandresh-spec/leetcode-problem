def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]

    left_recursion=merge_sort(left_arr)
    right_recursion=merge_sort(right_arr)

    return merge(left_recursion,right_recursion)



def merge(left,right):
    left_index=0
    right_index=0
    nums=[]

    while left_index< len(left) and right_index<len(right):
        if left[left_index]<= right[right_index]:
            nums.append(left[left_index])
            left_index+=1
        
        else:
            nums.append(right[right_index])
            right_index+=1
        

    nums.extend(left[left_index:])
    nums.extend(right[right_index:])

    return nums




import random
import time

n=int(input("enter the value n >=5000:  "))
arr=[]



for _ in range(n):
    arr.append(random.randint(0,5000))


print(*arr)
print("-"*40)


st_time=time.time()
sorted=merge_sort(arr)
end_time=time.time()


ex_time=(end_time-st_time)*1000

print(sorted)
print(ex_time)




            

