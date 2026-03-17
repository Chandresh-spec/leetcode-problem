# def longest_substring(s):
#     seen = {}
#     left = 0
#     max_len = 0

#     for right in range(len(s)):
#         if s[right] in seen:
#             left=seen[s[right]]+1
#         seen[s[right]]=right
#         max_len = max(max_len, right - left + 1)

#     return max_len



# st="acdeabcdef"
# print(longest_substring(st))



# def product_except_self(nums):
#     n = len(nums)
#     res = [1]*n
    
#     prefix = 1
#     for i in range(n):
#         res[i] = prefix
#         prefix *= nums[i]#corrected

#     postfix = 1
#     for i in range(n-1, -1, -1):
#         res[i] = postfix*res[i]
#         postfix *= nums[i]
    
#     return res




# n=nums = [1,2,3,4]
# print(product_except_self(nums))

# #expected=[24,12,8,6]



# def next_greater(nums):
#     stack = []
#     res = [-1]*len(nums)

#     for i in range(len(nums)-1,-1,-1):
#         while stack and nums[stack[-1]] <= nums[i]:
#             stack.pop()
#         if stack:
#             res[i]=nums[stack[-1]]
#         stack.append(i)

#     return res


# nums = [2,1,2,4,3]
# print(next_greater(nums))

# #expected [4,2,4,-1,-1]


def is_anagram(s, t):
    count = {}

    for c in s:
        count[c] = count.get(c,0) + 1
    
    for c in t:
        if c not in count:
            return False
        count[c] -= 1
    
    return True


s = "anagram"
t = "nagaram"
print(is_anagram(s,t))