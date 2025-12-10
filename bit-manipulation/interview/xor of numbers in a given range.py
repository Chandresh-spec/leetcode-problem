# XOR of numbers in a given range
# 
# 
# 0
# 
# 100
# Medium
# 
# Hints
# Given two integers L and R. Find the XOR of the elements in the range [L , R].
# 
# 
# Examples:
# Input : L = 3 , R = 5
# 
# Output : 2
# 
# Explanation : answer = (3 ^ 4 ^ 5) = 2.
# 
# Input : L = 1, R = 3
# 
# Output : 0
# 
# Explanation : answer = (1 ^ 2 ^ 3) = 0.









def findRangeXOR(l, r):
        #your code goes here
        xor=0
        for i in range(l,r+1):
            print(i)
            xor=xor^i
        

        return xor



l=1
r=3
# print(findRangeXOR(l,r))











def xorpattern(n):
        if n%4==1:
            return  1
        elif n%4==2:
              return n+1
        elif n%4==3:
              return 0
        else:
              return n
        
    


l=1
r=3
print(xorpattern(l-1)^xorpattern(r))
    