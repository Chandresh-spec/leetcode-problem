# def decimal_to_binary(num):
    # remainder=""
    # 
    # while int(num) >1:
        # val=num%2
        # if remainder=="":
# 
            # remainder+=str(val)
# 
        # else:
            # remainder=remainder+str(val)
        # 
        # num=num//2
    # 
    # remainder=remainder+"1"
    # 
    # return remainder[::-1]
            # 
# 
# num=13
# print(decimal_to_binary(num))


# 
# def binary_to_decimal(num):
    # total=0
    # p1=1
    # for i in range(len(num)-1,-1,-1):
# 
        # if num[i]=="1":
            # total+=p1
        # 
        # p1=p1*2
    # 
    # return total
# 
# 
# num="1101"
# print(binary_to_decimal(num))
# 



# and opertaor
num=13
print(num<<2)
