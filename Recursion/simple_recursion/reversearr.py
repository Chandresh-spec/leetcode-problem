def array(arr,index):
    n=len(arr)-1
    if index>n//2:
        return arr
    
    arr[index],arr[n-index]=arr[n-index],arr[index]
    return array(arr,index+1)


arr=[1,2,3,4,5]
print(array(arr,0))
