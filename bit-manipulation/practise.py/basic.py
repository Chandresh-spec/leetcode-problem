decimal="1101"

pow=1
count=0
for i in range(len(decimal)-1,-1,-1):
    if decimal[i]=="1":
        
        count+=pow

    pow=pow*2

       


print(count)
