















def cal(nums,goal):
        if goal < 0:
              return 0
        def binary_sum(goal):
            c_sum=0
            count=0
            r=0
            for i in range(len(nums)):
                c_sum=c_sum+nums[i]

                while c_sum >  goal :
                
                        c_sum -= nums[r]
                        r+=1
                count+= i - r+1
            return count
        return binary_sum(goal) - binary_sum(goal-1)
  


nums = [1,0,1,0,1]
goal=2
print(cal(nums,goal))