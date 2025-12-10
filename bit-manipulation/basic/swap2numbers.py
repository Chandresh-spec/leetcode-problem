#swap to  two numbers
a=5
b=6
a=a^b
b=a^b
a=a^b


# print(a,b)





#check ith bit is set or not


n=13
i=2

# new=(n&(1<<i))!=0
# 
# print(new)



# new=(n>>i)&1
# print(new)


#set the ith bit
# n=13
# i=1
# new=n|(1<<i)

# print(new)



#clear the ith bit

# 
# n=13
# i=3
# 
# print(n&~(1<<i))




#count the number of set bits

n=13
ans=0
while n >1:
    if n &1!=0:
        ans+=1
        

    n=n>>2

print(ans+1)



n=13
count=0
while n!=0:
    n=n&(n-1)
    count+=1

print(count)