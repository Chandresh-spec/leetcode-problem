def main_binary(arr,target):
    def binary_search(arr,target,first):

            lb=0
            ub=len(arr)-1
            n=-1
            ub=len(arr)-1
            while lb <= ub:
              mid=(ub+lb)//2
              if first:
                if arr[mid]==target:
                    n=mid
                    ub=mid-1
                else:
                    lb = mid+1
            return n
        

    first_1=binary_search(arr,target,True)
    if first_1 == -1:
       return 0
    second=binary_search(arr,target,False)


    return second-first_1

arr=[0, 0, 1, 1, 1, 2, 3]
target=1
print(main_binary(arr,target))