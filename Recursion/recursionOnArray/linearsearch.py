def linearsearch(arr,index,target):
    if index>len(arr)-1:
        return False
    
    if arr[index]==target:
        return True
    
    return linearsearch(arr,index+1,target)



arr=[4,5,6,9,8]
print(linearsearch(arr,0,99))