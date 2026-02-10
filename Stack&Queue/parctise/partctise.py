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
    
    


def isValid(s) -> bool:
        stack=[]
        for char in s:
            if char in "([{":
                stack.append(char)
            
            else:
                ele=stack.pop()
                if   (ele=="(" and char==")") or (ele=="{" and char=="}") or (ele=="[" and char=="]"):
                    continue
                return False
        return len(stack)==0




s ="(]"
print(isValid(s))
   