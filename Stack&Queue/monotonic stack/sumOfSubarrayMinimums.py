# def mono(arr):
    # total=0
    # for i in range(len(arr)):
        # stack=[]
        # for j in range(i,len(arr)):
            # while stack and stack[-1]>=arr[j]:
                # stack.pop()
            # 
            #    
            # 
        #    
        #   
            # 
            # stack.append(arr[j])
# 
            # if len(stack)==1:  
            #    total+=stack[-1]
    # 
    # return total
# 
# 
# 
# 
# 
# 
# 
# arr = [3,1,2,4]
# print(mono(arr))







def sumSubarrayMins(arr):
        total=0
        for i in range(len(arr)):
            current=arr[i]
            total+=current
            for j in range(i+1,len(arr)):
                if arr[j]< current:
                    current=arr[j]
                
                total+=current
        
        return current
    

arr = [3,1,2,4]
print(sumSubarrayMins(arr))