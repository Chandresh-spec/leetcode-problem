def f(num):
    if num==1:
        return 1
    return num*f(num-1)


num=5
print(f(num))