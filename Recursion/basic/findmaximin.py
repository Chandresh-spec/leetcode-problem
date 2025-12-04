def find_min_max(arr):
    if len(arr)==1:
        return arr[0],arr[0]
    
    mid=len(arr)//2

    left_arr=arr[:mid]
    right_arr=arr[mid:]

    left_max,left_min=find_min_max(left_arr)
    right_max,right_min=find_min_max(right_arr)

    total_max=max(left_max,right_max)
    total_min=min(left_min,right_min)

    return total_max,total_min



arr=[5,2,1,9,7,0]
print(find_min_max(arr))