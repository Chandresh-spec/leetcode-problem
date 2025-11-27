class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        arr=[-1]*n
        
        stack=[]
        for i in range(n*2-1,-1,-1):
            index=i%n

            while stack and stack[-1]<=nums[index]:
                stack.pop()
            
            if i < n:
                 if stack :
                     arr[index]=stack[-1]
            
            stack.append(nums[index])
        

        return arr