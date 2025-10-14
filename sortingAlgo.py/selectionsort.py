def selectionSort(arr):
    for i in range(len(arr)):
        mini=i
        for j in range(i+1,len(arr)):
            if arr[j]<  arr[mini]:
                mini=j
            
        
    
        arr[mini],arr[i]=arr[i],arr[mini]
    

    return arr




arr=[1,8,9,6,7,5,3,2]
print(selectionSort(arr))
