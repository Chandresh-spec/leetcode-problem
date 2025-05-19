def pallindrome(str1,index):
    n=len(str1)-1
    if index>=n//2:
        return True
    if str1[index]!=str1[n-index]:
        return False
    
    return pallindrome(str1,index+1)


str1="madal"
print(pallindrome(str1,0))