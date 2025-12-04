# def nse(nums):
    # stack=[]
    # n=len(nums)
    # arr=[n]*n
    # for i in range(n-1,-1,-1):
        # while  stack and nums[stack[-1]]>=nums[i]:
            # stack.pop()
        # 
        # arr[i]=stack[-1] if stack else n
# 
# 
        # stack.append(i)
    # 
    # return arr
# 
# 
# 
# def pse(nums):
    # stack=[]
    # n=len(nums)
    # arr=[n]*n
    # for i in range(n):
        # while  stack and nums[stack[-1]]>nums[i]:
            # stack.pop()
    #  
        # arr[i]=stack[-1] if stack else -1
        # stack.append(i)
#  
    # return arr
    # 
# 
# 
# 
# 
# def histogram(nums):
    # nse1=nse(nums)
    # pse1=pse(nums)
    # maxi=0
    # for i in range(len(nums)):
        # current=(nse1[i]-pse1[i]-1)*nums[i]
        # maxi=max(maxi,current)
    # return maxi

# nums=[2,4]
# print(histogram(nums))



from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        n=len(heights)
        maxi=0
        for i in range(len(heights)):
            while stack and heights[i]<=heights[stack[-1]]:
                current=stack.pop()
                height=heights[current]

                nse=i
                pse=stack[-1] if stack else -1
                width=nse-pse-1

                area=height*width

                maxi=max(maxi,area)
            stack.append(i)
            
        

        while stack:
            current=stack.pop()
            height=heights[current]
            nse=n
            pse=stack[-1] if stack else -1
            width=nse-pse-1
            area=height*width
            maxi=max(maxi,area)

        return maxi

        






