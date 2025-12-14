class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign=1
        if not s :
            return 0

        index=0
        if s[0]=="-":
            sign=-1
            index=1
        
        if s[0]=="+":
            index=1
        
        def helper(i,count):
            if i==len(s) or not s[i].isdigit():
                if count*sign>=2**31-1:
                    return 2**31-1
                if count*sign<=-2**31:
                    return -2**31
                
                return count*sign
            
            count=count*10+int(s[i])

            return helper(i+1,count)
        

        return helper(index,0)
        