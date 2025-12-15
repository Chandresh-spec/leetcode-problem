def check_sorted(arr,index):
    if len(arr)-1==index:
         return True
    

    if arr[index]>arr[index+1]:
         return False
    

    return check_sorted(arr,index+1)




arr=[1,9,3,4,5,6]
print(check_sorted(arr,0))
