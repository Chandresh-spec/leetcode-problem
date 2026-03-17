class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign=1
        if s[0]=='-':
            sign=-1
            s=s[1:]
        
        self.flag=False

        def helper(s,i,st):
            if i>=len(s):
                return st
            if s[i].isdigit():
                if s[i]=='0' and self.flag:
                    self.flag=True
                    st=st*10+int(s[i])
                else:
                   st=st*10+int(s[i])
                
            else:
                return st
            
            l= helper(s,i+1,st)
            l=l*sign

            if l >2**31:
                return 2**31
            if l < 2**31-1:
                return 2**31-1
        
            return l

            
        
        return helper(s,0,0)


l1=Solution()
l1.myAtoi("1337c0d3")