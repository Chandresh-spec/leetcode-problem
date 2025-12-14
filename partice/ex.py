#and or xor  swift(right shift<<)





# result = number >> shift_count




# print(12&3)

# n=13
# i=1

# if 1&(n>>i)==0:
#     print(False)
# else:
#     print(True)



# 
n=13
count=0
while n!=0:
    n=n&(n-1)
    count+=1
    
    


print(count)
n=13
if n==1 or n==2 or n==3:
    print("Prime")

if n%2==0 or n %3==0:
    print("Not pRIME")
else:
    print("prime")


