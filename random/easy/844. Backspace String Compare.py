def backspaceCompare(s,t):
        # stack=[]
        # stack2=[]

        # for i in s:
        #     if i=="#" and stack:
        #         stack.pop()
            
        #     elif i!="#":
        #         stack.append(i)
        

        # for i in t:
        #     if i=="#" and stack2:
        #         stack2.pop()
            
        #     elif i!="#":
        #         stack2.append(i)
        

        # return stack==stack2
        r=0

        for i in range(len(s)):
            if s[i]=="#":
                    while s[r]=="#":
                           r+=1
                    r+=1
        

        
        str1=""
        for char in s[r:len(s)]:
               if char!="#":
                      str1+=char
        
        print(str1)
        
        r2=0
        for j in range(len(t)):
            if t[j]=="#":
                    while s[r2]=="#":
                           r2+=1
                    r2+=1
                
            
        str2=""
        for char in s[r:len(t)]:
               if char!="#":
                      str2+=char
        
        print(str1,str2)
        return str1==str2
        

        # return val1==val2
                    
                



s = "xywrrmp"
t = "xywrrm#p"

print(backspaceCompare(s,t))