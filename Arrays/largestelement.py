
# Largest Element
# 
# Easy
# 
# Given an array of integers nums, return the value of the largest element in the array
# 
# 
# Examples:
# Input: nums = [3, 3, 6, 1]
# 
# Output: 6
# 
# Explanation: The largest element in array is 6
# 
# Input: nums = [3, 3, 0, 99, -40]
# 
# Output: 99
# 
# Explanation: The largest element in array is 99

# Input: nums = [-4, -3, 0, 1, -8]

def largest(arr):
    largest=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                if arr[j]>largest:
                    largest=arr[j]
        
    return largest  

# Time Complexity=o(n2)
# 

arr=[-4, -3, 0, 1, -8]


print(largest(arr))





def largest_sort(arr):
    arr.sort()
    return arr[-1]




arr=[3, 3, 0, 99, -40]


print(largest_sort(arr))


# Time Complexity=o(nlog n)
# 





def largest_ele(arr):
    largest=arr[0]
    for i in arr:
        if i > largest:
            largest=i
    
    return largest



arr=[3, 200, 0, 99, -40]


print(largest_ele(arr))

# 
# Time Complexity=o(n)

