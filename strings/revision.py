# def reverseWord(s):
    # ans=""
    # cur=""
    # for char in s:
        # if char!=" ":
            # cur+=char
        # else:
            # if cur!="":
                # if ans=="":
                    # ans+=cur
                # else:
                    # ans=cur+" "+ans
                # cur=""
    # 
    # if cur:
        # if ans=="":
            # ans+=cur
        # else:
            # ans=cur+" "+ans
        # 
    # return ans
# 
# 
# 
# s="the sky is blue"
# print(reverseWord(s))


def largestodd(nums):
    largest=-1
    for i in range(len(nums)):
        num=int(nums[i])
        if num%2==1:
            largest=i
        
    if largest== -1:
        return ""
    return nums[:largest+1]



nums="52"
print(largestodd(nums))





class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            ele=int(num[i])

            if ele%2==1:
                return num[:i+1]
        
        return ""