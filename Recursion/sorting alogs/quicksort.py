def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

    
def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    for j in range(low+1,high+1):
        if arr[j]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i-1],arr[low]=arr[low],arr[i-1]

    return i-1


arr=[3,5,2,7,8,1,9]
quicksort(arr,0,len(arr)-1)
print("sorted array",arr)