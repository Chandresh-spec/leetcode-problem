from typing import List

def minDays(bloomDay: List[int], m: int, k: int) -> int:

        def f(current,bloomDay,m,k):
            count=0
            for i in bloomDay:
                if i <= current:
                    count+=1
                    if count ==k:
                        m-=1
                        count=0

                else:
                    count=0
            
            return m<=0
        for i in range(len(bloomDay)):
            if f(bloomDay[i],bloomDay,m,k):

                return bloomDay[i]
        return -1
        


bloomDay = [1000000000,1000000000]
m =1
k=1
print(minDays(bloomDay,m,k))


        