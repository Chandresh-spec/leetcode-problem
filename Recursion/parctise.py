def print_name(n):
    if n<1:
        return
    
    print_name(n-1)
    print(n)



# n=5
# print_name(n)




# sum of  first n number

# 
# def helper(n):
    # if n ==1:
        # return 1
    # return n+helper(n-1)
# 
# 
# 
# n=5
# print(helper(n))




num=40
count=0



def atoi(s):
    s=s.strip()
    zero=False
    count=0
    sign= -1 if s[0]=="-" else 1


    def helper(index,count,zero):
        if index==len(s):
            if count==0:
                return count

            return  count*sign
        
        if s[index] in ["0","1","2","3","4","5","6","7","8","9"]:
            if s[index]!=0 or zero:
                count=count*10+int(s[index])
                zero=True
        else:
            return count
        


        return helper(index+1,count,zero)

    
    return  helper(0,count,zero)
    


s= "words and 987"
print(atoi(s))

                
            

