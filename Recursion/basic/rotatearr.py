def helper(arr,n,index):
        if index>=n//2:
            return arr
            
        arr[index],arr[n-index-1]=arr[n-index-1],arr[index]
        return helper(arr,n,index+1)
        
       



arr= [1,2,3,4,5]
n=5
print(helper(arr,n,0))