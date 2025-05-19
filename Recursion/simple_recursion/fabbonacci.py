def fib(num):
    if num <=1:
        return num
    return fib(num-1)+fib(num-2)


num=4
print(fib(num))