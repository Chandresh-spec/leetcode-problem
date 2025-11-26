def quicksort(nums,low,high):
    if low < high:
        pi=partition(nums,low,high)

        quicksort(nums,low,pi-1)
        quicksort(nums,pi+1,high)

    


def partition(nums,low,high):

    pivot=nums[low]

    i=low+1
    for j in range(low+1,high+1):
        if nums[j] < pivot:
            nums[i],nums[j]=nums[j],nums[i]
        
            i+=1
    

    nums[low],nums[i-1]=nums[i-1],nums[low]


    return i-1


import  time
import  random

n=int(input("enter the number of element n >5000"))
arr=[]
for i in range(n):
    arr.append(random.randint(0,5000))


print(arr)
print("_"*500)


st_time=time.time()
quicksort(arr,0,len(arr)-1)
end_time=time.time()

ex_time=(end_time-st_time)*1000

print(arr)
print(ex_time)
