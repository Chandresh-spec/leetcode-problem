# Kth element of 2 sorted arrays


# 0

# 100
# Medium

# Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.


# Examples:
# Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5

# Output: 6

# Explanation: The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

# Input: a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7

# Output: 256

# Explanation: Final sorted array is - [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892], 7th element of this array is 256.

# Input: a = [2, 3, 6], b = [7, 9], k = 4





from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def median(a,b,k):
            if len(a)>len(b):
                return median(b,a,k)
            

            n1=len(a)
            n2=len(b)

            low,high=0,n1

            while low <= high:
                cut1=(low+high)//2
                cut2=abs(cut1-k)


                l1 = float('-inf') if cut1 == 0 else a[cut1 - 1]
                l2 = float('-inf') if cut2 == 0 else b[cut2 - 1]
                r1 = float('inf') if cut1 == n1 else a[cut1]
                r2 = float('inf') if cut2 == n2 else b[cut2]



                if l1<= r2 and l2<= r1:
                         return max(l1, l2) 
            
            
                
                elif l1> r2:
                    high = cut1 - 1
                

                else:
                    low = cut1 + 1



        return median(nums1,nums2,5)
            
      
         



        







         


        