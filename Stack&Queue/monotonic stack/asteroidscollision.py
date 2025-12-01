

def asteroidCollision(asteroids):
        stack=[]
        for i in range(len(asteroids)):
            while stack and stack[-1]>0 and asteroids[i]<0:
                if stack[-1]<asteroids[i]:
                    stack.pop()
                    continue
                
                if stack[-1]==asteroids[i]:
                    stack.pop()
                break
        
            else:
               stack.append(asteroids[i])
        
        return stack


asteroids =[5,10,-5]
print(asteroidCollision(asteroids))