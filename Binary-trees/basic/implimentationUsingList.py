

def preorder(arr,index):
    if  index >=len(arr) or not arr[index] :
        return
    
    print(arr[index])
    preorder(arr,2*index+1)
    preorder(arr,2*index+2)



arr=[10,20,30,40,50,60,70]
print(preorder(arr,0))