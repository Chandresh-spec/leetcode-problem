class stack:
    def __init__(self):
        self.stack=[]


    

    def is_empty(self):
        if len(self.stack)==0:
            return True
        return False
    
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]
    

    def push(self,value):
        self.stack.append(value)
        return f"{value} is appended,{self.stack}"
    
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        
        value=self.stack.pop()
        return f"{value} is popped form stack"
    

#implement the queue using Array



s1=stack()
print(s1.is_empty())
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.stack)
s1.pop()
print(s1.stack)
print(s1)





#implement the queue using Array
class Queue:
    def __init__(self):
        self.q=[]
    

    
    