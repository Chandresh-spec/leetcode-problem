
# Easy
# Topics
# # premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longest_prefix(str1):
    prefix=str1[0]


    for s in str1:
        while not s.startswith(prefix):
            prefix=prefix[:-1]
            if not prefix:
                return "" 
    

    return prefix
              








str1=["flower","flow","flight"]
print(longest_prefix(str1))


