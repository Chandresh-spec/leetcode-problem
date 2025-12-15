def findmin(arr,index):
    if index >= len(arr)-1:
        return arr[index]
    

    return min(arr[index],findmin(arr,index+1))


arr=[1,5,8,9,63,0]
print(findmin(arr,0))
