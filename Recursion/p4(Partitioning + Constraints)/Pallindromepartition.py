#  131. Palindrome Partitioning
# Solved
# Medium
# Topics
# Companies
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.












def partition(s):
        ans=[]
        def helper(index,ds):
            if len(s)==index:
                ans.append(ds[:])
            
            for i in range(index,len(s)):
                if ispallindrome(s,index,i):
                    ds.append(s[index:i+1])
                    helper(i+1,ds)
                    ds.pop()
        def ispallindrome(s,index,i):
            while index<=i:
                if s[index]!=s[i]:
                    return False
                index+=1
                i-=1
            return True
                
        helper(0,[])
        return ans


s="aabb"
print(partition(s))