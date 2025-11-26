class Stack:
    def __init__(self):
        self.stack=[]
        
    

    def __str__(self):
        val=[str(x) for x in reversed(self.stack)]
        return "\n".join(val)
    
    

    def isEmpty(self):
        if self.stack==[]:
            return True
        
        else:
            return False


    def push(self,value):
         self.stack.append(value)
         print("value added")
        
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        val=self.stack.pop()
        return f"{val} is popped form stack"
    

    def peek(self):
        if self.isEmpty():
            return "stack is empty"

        return self.stack[-1]


s1=Stack()
print(s1.isEmpty())
s1.push(1)
s1.push(2)
s1.push(3)
print(s1.pop())
print(s1.peek())
s1.stack()