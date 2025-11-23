def print_name(n):


    if n<=0:
        return 
    
    
    print_name(n-1)
    print(n)





print(print_name(5))