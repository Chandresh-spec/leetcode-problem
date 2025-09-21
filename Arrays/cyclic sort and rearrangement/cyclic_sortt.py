# What is Cyclic Sort?

# Cyclic sort is a special sorting technique used when:

# The array contains numbers in a known range → usually 1..n or 0..n.

# We want to rearrange elements to their correct position without using extra space.

# 👉 Idea:

# If a number is not at its correct index, swap it with the number that is currently at its target index.

# Keep doing this until every number is at the correct index




def cyclic_sort(nums):
    n=len(nums)
    i=0
    while i < n:
        corret_index=nums[i]-1
        if  nums[i] !=nums[corret_index]:
            nums[i],nums[corret_index]=nums[corret_index],nums[i]
        
        else:
            i+=1
    
    return nums






nums=[3, 1, 5, 4, 2]
print(cyclic_sort(nums))