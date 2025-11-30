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
        
        return total
    

# arr = [3,1,2,4]
# print(sumSubarrayMins(arr))






def  nse(nums):
     stack=[]
     n=len(nums)
     arr=[0]*n

     for i in range(n-1,-1,-1):
            while stack and stack[-1]>= nums[i]:
               stack.pop()
            

            arr[i]=stack[-1]if stack else n

            stack.append(nums[i])
        
     return arr



def pse(nums):
    stack=[]
    n=len(nums)
    arr=[0]*n

    for i in range(len(nums)):
        while stack and stack[-1]>=nums[i]:
              stack.pop()
        
     
        arr[i]=stack[-1]if stack else -1

        stack.append(nums[i])
    
    return arr




def subarray(nums):
    nse1=nse(nums)
    pse1=pse(nums)
    total=0

    for i in range(len(nums)):
         
         left=i-pse1[i]

         right=nse1[i]-i


         freq=(left*right)*1

         val=(freq*nums[i])

        
    return total
                        
            
arr = [11,81,94,43,3]
print(subarray(arr))