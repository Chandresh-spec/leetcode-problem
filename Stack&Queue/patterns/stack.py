# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack=[]
#         for char in s:
#             if char != "]":
#                 stack.append(char)
            
#             else:
#                 substr=""
#                 while stack and  stack[-1].isalpha():
#                     ch=stack.pop()

#                     substr=ch+substr
#                 stack.pop()
#                 num=""
#                 while stack and stack[-1].isdigit():
#                     num=stack.pop()+num
                
#                 stack.append(substr*int(num))
            
        
#         return "".join(stack)



# def  NextGreaterElementI(nums1,nums2):
#     stack=[]
#     hashmap={}
#     for i in range(len(nums2)-1,-1,-1):
          
#         while stack and stack[-1]<nums2[i]:
#             stack.pop()
        
#         if stack:
#             hashmap[nums2[i]]=stack[-1]
        
#         stack.append(nums2[i])
    

#     arr=[-1]*len(nums1)
#     for i in range(len(nums1)):
#         if nums1[i] in hashmap:
#             arr[i]=hashmap[nums1[i]]
        

#     return arr
    

        


# nums1 = [4,1,2]
# nums2 = [1,3,4,2]

# print(NextGreaterElementI(nums1,nums2))





def nextGreaterELement2(nums):
        n=len(nums)
        arr=[-1]*len(nums)
        stack=[]

        # for i in range(len(nums)):
        #     for j in range(i,n*2):
        #         j=j%n
        #         if nums[j]>nums[i]:
        #              arr[i]=nums[j]
        #              break
        
        # return arr
        for i in range(n*2-1,-1,-1):
                while stack and nums[i%n]>=stack[-1]:
                        stack.pop()
                
                if i < n:
                        if stack:
                                arr[i]=stack[-1]
                
                stack.append(nums[i%n])
        
        return arr
                
nums =[1,2,1]

print(nextGreaterELement2(nums))      
