#swap to numbers
a=5
b=6
a=a^b
b=a^b
a=a^b


print(a,b)





#check ith bit is set or not


n=13
i=2

new=(n&(1<<i))!=0

print(new)