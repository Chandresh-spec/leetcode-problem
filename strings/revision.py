def reverseWord(s):
    ans=""
    cur=""
    for char in s:
        if char!=" ":
            cur+=char
        else:
            if cur!="":
                if ans=="":
                    ans+=cur
                else:
                    ans=cur+" "+ans
                cur=""
    
    if cur:
        if ans=="":
            ans+=cur
        else:
            ans=cur+" "+ans
        
    return ans



s="the sky is blue"
print(reverseWord(s))
