# def alternateDigitSum(n: int) -> int:
#         count=0
#         n=str(n)
#         for i in range(len(n)):
#             if i%2==0:
#                 count=count+int(n[i])
            
#             else:
#                 count=count+(-int(n[i]))
        
#         return count



# n = 521
# print(alternateDigitSum(n))


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        count=0
        temp=n

        while temp>0:
            count+=1
            temp//=10
        
        sum_of=0
        while n>0:
            if count%2==0:
                sum_of+=n%10
            else:
                sum_of-=n%10
            
            count-=1
            n//=10
            
        return -sum_of
