
def lengthOfLongestSubstring(s):
        st=0
        maxi=0
        hashmap={}
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]]>=st:
                st=hashmap[s[i]]+1
            
            hashmap[s[i]]=i
            maxi=max(maxi,i-st+1)
        return maxi




s="abba"
print(lengthOfLongestSubstring(s))