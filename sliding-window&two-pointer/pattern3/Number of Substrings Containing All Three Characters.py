# 1358. Number of Substrings Containing All Three Characters
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
# Example 3:

# Input: s = "abc"
# Output: 1






class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashmap={"a":-1,"b":-1,"c":-1}
        count=0
        for i in range(len(s)):
            hashmap[s[i]]=i
            if (hashmap['a']!= -1 and hashmap['b']!= -1 and hashmap['c']!= -1):
                count+=1+(min(hashmap['a'],hashmap['b'],hashmap['c']))
            
        return count

        
            
            
        