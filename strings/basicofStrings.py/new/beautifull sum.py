class Solution:
    def beautySum(self, s: str) -> int:
        count=0
        hashmap={}
        for i in range(len(s)):
            hashmap={}
            for j in range(i,len(s)):
                hashmap[s[j]]=hashmap.get(s[j],0)+1

                mini=min(hashmap.values())
                maxi=max(hashmap.values())

                if mini!=maxi:
                    count+=maxi-mini
                

        return count






hashmap={"c":1,"d":4,"p":0}

new=sorted(hashmap.items(),key=lambda y:y[1])
print(new)