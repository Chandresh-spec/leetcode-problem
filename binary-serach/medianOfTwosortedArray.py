# 4. Median of Two Sorted Arrays
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106





# brute approach

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left=0
        right=0
        arr=[]
        while left <len(nums1) and right < len(nums2) :
            if nums1[left]<= nums2[right]:
               arr.append(nums1[left])
               left+=1
            else:
                arr.append(nums2[right])
                right+=1
            
        arr.extend(nums1[left:])
        arr.extend(nums2[right:])


        if len(arr)%2==1:
             return arr[len(arr)//2]
            
        else:
           
            return (arr[len(arr)//2]+arr[len(arr)//2-1])/2
        
         


# 
# Time complexity is o(n+m)
# space complexity is o(n+m)



# better appraoch



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        mid=(n+m)//2

        prev=cur=0
        count=0
        left=right=0

        while count <= mid:
            prev=cur

            if left  < n and(right>=m or  nums1[left]<=nums2[right]):
                cur=nums1[left]
                left+=1
            elif right  < m and(left>=n or  nums2[right] < nums1[left]):
                cur=nums2[right]
                right+=1
            

            count+=1
        


        if (n+m) %2==1:
            return cur
        
        else:
            return (cur+prev)/2





# Time complexity is o(n+m)
# space complexity is o(1)    reduce space using hypothesis index   
        
            
      
         



        







         


        






         


        