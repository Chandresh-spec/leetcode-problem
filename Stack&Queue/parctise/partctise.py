# class stack:
#     def __init__(self):
#         self.stack=[]
    
#     def isempty(self):
#         if self.stack==[]:
#             return True
#         return False

#     def push(self,value):
#         self.stack.append(value)
#         print(f" {value} is appened  to stack sucessfully")
#         print(self.stack)
    
#     def pop(self):
#         if self.isempty():
#             return "stack is empty"
#         val=self.stack[-1]
#         self.stack.pop()
#         print(f"{val} is poped from stack")
    

#     def peek(self):
#         if self.isempty():
#             return "stack is empty"
#         return stack[-1]
    
    


def decode(s):
    stack=[]
    for char in s:
        if char != "]":
            stack.append(char)
        
        else:
            substr=""
            while stack and  stack[-1].isalpha() :
                ch=stack.pop()

                substr=ch+substr
            
            stack.pop()
            num=""
            while stack and not stack[-1].isdigit():
                num=stack.pop()+num
                
            
            stack.append(substr*int(num))
        
    
    return stack




s ="abc3[cd]xyz"
print(decode(s))

                

   