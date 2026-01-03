
def shipWithinDays(weights,days):



        def check(j,weights,days):
            sum_of=0
            count=1

            for i in range(len(weights)):
                if weights[i]+sum_of <=j:
                    sum_of+=weights[i]
                else:
                    count+=1
                    sum_of=weights[i]
            
            return count==days







        lb,ub=min(weights),sum(weights)
        for i in range(lb,ub):
            if check(i,weights,days):
                return i
        
        return -1




weights = [1,2,3,1,1]
days = 4
print(shipWithinDays(weights,days))