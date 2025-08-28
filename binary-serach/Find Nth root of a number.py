# Find Nth root of a number


# 0

# 100
# Medium

# Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.


# Examples:
# Input: N = 3, M = 27

# Output: 3

# Explanation: The cube root of 27 is equal to 3.

# Input: N = 4, M = 69

# Output:-1

# Explanation: The 4th root of 69 does not exist. So, the answer is 



def NthRoot(n,m):
      low=0
      high=m
      ans=-1

      def f(mid,n):
          res=1
  
          for _ in range(n):
            res *=mid
          return res

      while low<= high:
        mid=(high+low)//2

        if f(mid,n)== m:
           return mid
        elif f(mid,n)<m:
           low=mid+1
        else:
          high=mid-1
        
      return ans

N = 3
M = 20
print(NthRoot(N,M))

      