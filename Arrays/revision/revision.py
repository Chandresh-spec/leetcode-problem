def largest_element(nums):
    # largest_element=float('-inf')
    # for i in nums:
        # if i > largest_element:
            # largest_element=i
        # 
    # 
    # return largest_element

    nums.sort(reverse=False)

    return nums
    




nums=[1,8,9,6,3,1]
print(largest_element(nums))

#o(n)



