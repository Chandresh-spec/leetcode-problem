# 424. Longest Repeating Character Replacement
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length


def characterReplacement(s: str, k: int) -> int:
        maxi_freq=0
        hashmap={}
        st=0
        maxi=0
        for i in range(len(s)):
            hashmap[s[i]]=hashmap.get(s[i],0)+1
            maxi_freq=max(hashmap.values())
            if (i-st+1)-maxi_freq > k:
                hashmap[s[st]] -= 1
                st+=1
            
            maxi=max(maxi,i-st+1)
        
        return maxi

s = "AABABBA"
k = 1
print(characterReplacement(s,k))