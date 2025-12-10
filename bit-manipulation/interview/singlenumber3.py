class Solution:   
    def singleNumber(self, nums):
        #your code goes 
        xor=0
        for num in nums:
            xor=xor^num
        
        dif=xor&(xor-1)^xor

        b1=0
        b2=0
        for num in nums:
            if dif &num:
                b1=b1^num
            else:
                b2=b2^num
        

        return [b1,b2]