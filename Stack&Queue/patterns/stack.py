class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char != "]":
                stack.append(char)
            
            else:
                substr=""
                while stack and  stack[-1].isalpha():
                    ch=stack.pop()

                    substr=ch+substr
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                
                stack.append(substr*int(num))
            
        
        return "".join(stack)
