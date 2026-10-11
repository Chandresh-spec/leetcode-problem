
# def removeDuplicates(nums) -> int:
#         hashmap={}
#         index=0
#         for i in range(len(nums)):

#             if nums[i] not in hashmap:
#                 nums[index],nums[i]=nums[i],nums[index]
#                 hashmap[nums[index]]=1
#                 index+=1
            

#         return nums


# nums=[0,0,1,1,1,2,2,3,3,4]
# print(removeDuplicates(nums))




# def missingNumber(nums) -> int:
#         for i in range(len(nums)):
#             correct_place=nums[i]

#             if correct_place <= len(nums)-1 and i !=nums[correct_place]:
#                 nums[i],nums[correct_place]=nums[correct_place],nums[i]
        

#         return nums
        
#         # for i in range(len(nums)):
#             # if nums[i]!=i:
#                 # return i
#         # 
#         # return i+1
#         # 
# # 
# nums=[9,6,4,2,3,5,7,0,1]
# print(missingNumber(nums))





# def rotate(nums,k) -> None:
#         """
#         Do not return anything, modify nums in-place instead.

#         """
#         n=len(nums)
#         arr=[0]*n
#         j=0

#         for i in range(n-k,n):
#             arr[j]=nums[i]
#             j+=1
        
#         for i in range(n-k):
#             arr[j]=nums[i]
#             j+=1
        

#         return arr
        
        
    
# nums=[1,2,3,4,5,6,7]
# k=3
# print(rotate(nums,k))
       





# def unionArray(nums1, nums2):

#         # lookup=set()
#         # arr=[]
#         # for num in nums1:
#         #     if num not in lookup:
#         #         lookup.add(num)
        


#         # for num in nums2:
#         #     if num not in lookup:
#         #         lookup.add(num)
        


#         # for i in lookup:
#         #     arr.append(i)
        

#         # arr.sort()
#         # return arr

#         arr=[]
#         l1=0
#         l2=0
#         previous=None

#         while l1<len(nums1) and l2<len(nums2):
#                 if nums1[l1]<=nums2[l2]:
#                     if previous==None or nums1[l1]!=previous:
#                             arr.append(nums1[l1])
#                             previous=nums1[l1]
                        
#                     l1+=1
#                 else:
#                     if previous==None or nums2[l2]!=previous:
#                                 arr.append(nums2[l2])
#                                 previous=nums2[l2]
                        
#                     l2+=1
            
        

#         while l1<len(nums1) :
#                     if previous==None or nums1[l1]!=previous:
#                             arr.append(nums1[l1])
#                             previous=nums1[l1]
                        
#                     l1+=1
        
#         while l2<len(nums2):
#                 if previous==None or nums2[l2]!=previous:
#                                 arr.append(nums2[l2])
#                                 previous=nums2[l2]
                        
#                 l2+=1

        
#         return arr
            
        
               
    

        
        


# nums1 = [3, 4, 4, 4]
# nums2 = [6, 7, 7]
# print(unionArray(nums1,nums2))


    
        

        
            
        
    



# def missingNumber(nums):

#         # for i in range(len(nums)+1):
#         #         found=False
#         #         for num in nums:
#         #                 if i ==num:
#         #                         found=True

#         #         if not found:
#         #                 return i


#         # xor=0
#         # for i in range(len(nums)+1):
#         #         xor=xor^i
        
#         # for i in nums:
#         #         xor^=i

#         # return xor



#         i=0
#         while i< len(nums):
#                 correct_index=nums[i]
#                 if i>correct_index and nums[correct_index]!=nums[i]:
#                         nums[correct_index],nums[i]=nums[i],nums[correct_index]
                
#                 else:
#                         i+=1
        
        
#         for i in range(len(nums)):
#                 if i!=nums[i]:
#                         return i
#         return i+1

                
# nums = [0, 2, 3, 1, 4]
# print(missingNumber(nums))





# def longestSubarray(nums, k):
    # maxi=0
    
    # for i in range(len(nums)):
    #     sum_of=0
    #     count=0
    #     for j in range(i,len(nums)):
    #         sum_of+=nums[j]


            
    #         if sum_of>k:
    #             break

    #         if sum_of==k:
    #             maxi=max(maxi,count)
            
    #         count+=1
    
    # return maxi






#  nums = [10, 5, 2, 7, 1, 9]
#  k=15
# print(longestSubarray(nums,k))
    



# def sortColors(nums):
        
#         count1=0
#         count2=0
#         count3=0
#         for clr in nums:
#             if clr==0:
#                 count1+=1
#             elif clr==1:
#                 count2+=1
#             else:
#                 count3+=1
#         # return[count1,count2,count3] 
        

#         j=0
#         for i in range(count1):
#             nums[j]=0
#             j+=1
        
#         for i in range(count2):
#             nums[j]=1
#             j+=1
        
#         for i in range(count2):
#             nums[j]=2
#             j+=1
        

#         return nums



# nums = [1]
# print(sortColors(nums))



# hashmap={}

# nums=[2,2,1,1,1,2,2]
# n=len(nums)
# for i in range(len(nums)):
#       hashmap[nums[i]]=hashmap.get(nums[i],0)+1
    

# i=j=0
# for value,count in hashmap.items():
#     if count>i:
#             i=count
#             j=value

# print(i,j)
# if count>=n//2:
#     print (value)




# def threesum(nums):
#     nums.sort()#[-4,-1,-1,0,1,2]

#     ans=[]
#     n=len(nums)
#     for i in range(n):

#         j=i+1
#         k=n-1

#         while j<=k:
#             if nums[i]+nums[j]+nums[k]==0:
#                 temp=[nums[i],nums[j],nums[k]]
#                 ans.append(temp)


#             while nums[i]==nums[j] and i!=j:
#                 j+=1
            

#             while nums[j]==nums[k] and k!=j:
#                 k-=1

#             k-=1


#     return ans




# nums = [-1,0,1,2,-1,-4]

# print(threesum(nums))



# name="harry"
# print(name[-4:2])







# def fourSum(nums,target):
#         n=len(nums)
#         st=set()
#         for a in range(n):
#             for b in range(a+1,n):
#                 hashmap={}
#                 for c in range(b+1,n):
                    
#                     sum_of= -(nums[a]+nums[b]+nums[c])
#                     total_remain=target-(sum_of)
                  
#                     if total_remain in hashmap:
#                         temp=[nums[a],nums[b],nums[c],sum_of-target]
#                         temp.sort()
#                         st.add(tuple(temp))
                    
#                     hashmap[nums[c]]=nums[c]
        

#         ans=[list(item) for item in st]
#         return ans



# nums = [2,2,2,2,2]
# target = 8
# print(fourSum(nums,target))





def maxlen(nums):
    maxi=0
    n=len(nums)
    for i in range(n):
        count=0
        for j in range(i,n):
            if count+nums[j]==0:
                maxi=max(maxi,j-i+1)

            count+=nums[j]


    return maxi



arr = [1, 0, -4, 3, 1, 0]
print(maxlen(arr))
