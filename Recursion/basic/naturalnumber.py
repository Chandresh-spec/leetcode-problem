def natural_num(num):
    if num<=0:
        return 0
    
    return num+natural_num(num-1)




num=4
print(natural_num(num))