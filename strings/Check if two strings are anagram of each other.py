def isAnagram( s, t):
        if len(s)!=len(t):
            return False
        hashmap1={}
        hashmap2={}
        for i in range(len(s)):
           hashmap1[s[i]]= hashmap1.get(s[i],0)+1
           hashmap2[t[i]]=hashmap2.get(t[i],0)+1
        
        return hashmap1==hashmap2
        



s = "rat"
t = "car"
print(isAnagram(s,t))