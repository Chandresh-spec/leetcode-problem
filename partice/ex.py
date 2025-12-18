#and or xor  swift(right shift<<)





# result = number >> shift_count




# print(12&3)

# n=13
# i=1

# if 1&(n>>i)==0:
#     print(False)
# else:
#     print(True)



# 
# n=13
# count=0
# while n!=0:
    # n=n&(n-1)
    # count+=1
    # 
    # 


# print(count)
# n=13
# if n==1 or n==2 or n==3:
    # print("Prime")

# if n%2==0 or n %3==0:
    # print("Not pRIME")
# else:
    # print("prime")




# def validpallindrome(s):
    # char=""
    # for i in s:
        # if i.isalnum():
        # 
            # char+=i.lower()
# 
    # print(char) 
    # lb=0
    # ub=len(char)-1
# 
    # while lb <= ub :
        # if char[lb]!=char[ub]:
            # return False
        # 
# 
        # lb+=1
        # ub-=1
        # 
    # 
# 
    # return True










# class Solution:
    # def isPalindrome(self, s: str) -> bool:
        # s=s.strip()
        # left,right=0,len(s)-1
# 
# 
        # while left< right:
            # while not s[left].isalnum() and left < right:
                # left+=1
            # 
# 
            # while not s[right].isalnum() and left<right:
                # right-=1
            # 
# 
# 
            # if s[left].lower()!=s[right].lower():
                # return False
# 
            # right-=1
            # left+=1
# 
        # 
        # return True
# 
        # 



#  kadness algorithm

def maxSubArray(nums):
        maxi=float('-inf')
        count=0
        for i in nums:
            count+=i
            maxi=max(maxi,count)
            if count<0:
                count=0
            
        
        return maxi


nums=[1]
print(maxSubArray(nums))



