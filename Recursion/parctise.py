def natural_Number(n,total):
    if n==0:
        return total
        
    
    natural_Number(n-1,total+n)




n=5
print(natural_Number(n,0))




