# You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.



# Return the count of occurrences of target in the array.


# Examples:
# Input: arr = [0, 0, 1, 1, 1, 2, 3], target = 1

# Output: 3

# Explanation: The number 1 appears 3 times in the array.

# Input: arr = [5, 5, 5, 5, 5, 5], target = 5

# Output: 6

# Explanation: All elements in the array are 5, so the target appears 6 times.

# Input: arr = [2, 4, 6, 8, 10], target = 





class Solution:
    def countOccurrences(self, arr, target):
        # Your code goes here

        def Binary_search(nums,target,first):
            lb=0
            ub=len(nums)-1
            ans=-1

            while lb <= ub:
                mid=(ub+lb)//2

                if nums[mid]==target:
                    if first:
                        ans=mid
                        ub=mid-1
                    else:
                        ans=mid
                        lb=mid+1
                elif nums[mid] > target:
                    ub=mid-1
                else:
                    lb= mid+1
            return ans

        
        first=Binary_search(arr,target,True)
        if first == -1:
            return 0
        last=Binary_search(arr,target,False)

        return  last-first+1
        


                