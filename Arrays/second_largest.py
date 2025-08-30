# Second Largest Element
# 
# 
# 
# Easy
# 
# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.
# 
# 
# Examples:
# Input: nums = [8, 8, 7, 6, 5]
# 
# Output: 7
# 
# Explanation: The largest value in nums is 8, the second largest is 7
# 
# Input: nums = [10, 10, 10, 10, 10]
# 
# Output: -1
# 
# Explanation: The only value in nums is 10, so there is no second largest value, thus -1 is returned
# 
# Input: nums = [7, 7, 2, 2, 10, 10, 10]
# 


def second_largest(arr):
    largest=-1
    second=-1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                if arr[j]>largest:
                    largest=arr[j]

                if arr[j]<largest and arr[j]>second:
                    second=arr[j]
        
    return second

# Time Complexity=o(n2)
# 

arr= [7, 7, 2, 2, 10, 10, 10]


print(second_largest(arr))




def largest_ele(arr):
    largest=arr[0]
    second=-1
    for i in arr:
        if i > largest:
            second=largest
            largest=i
        elif i> second and i != largest:
            second=i
        

       
       
    
    return second







arr= [ 10, 10, 10]


print(largest_ele(arr))

# 
# Time Complexity=o(n)