# def longest_subarray_len(nums):

#     maxi=0
#     for i in range(len(nums)):
#         count=0
#         for j in range(i,len(nums)):
#             count+=nums[j]

#             if count==0:
#                 maxi=max(maxi,j-i+1)
    

#     return maxi


# nums=   [1, 0, -4, 3, 1, 0]

# print(longest_subarray_len(nums))



def longest(arr):
    hashmap={0:-1}
    maxi=0
    sum_of=0
    for i in range(len(arr)):
        sum_of+=arr[i]

        if sum_of in hashmap:
            maxi=max(maxi,i-hashmap[sum_of])
        else:
           hashmap[sum_of]=i
    return maxi

nums=  [15, -2, 2, -8, 1, 7, 10, 23]
print(longest(nums))