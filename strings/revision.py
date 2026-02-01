def reverseString(s):
    temp=""
    ans=""
    for char in s :
        if char !=" ":
            temp+=char
        
        else:
            if temp!=" ":
                if ans !="":
                    ans=temp + " "+ans
                
                else:
                    ans+=temp
            
            temp=""
        
    
    if temp:
        if ans !="":
            ans=temp + " "+ans
        else:
            ans+=temp
    return ans


s=  "  hello world  "
print(reverseString(s))
