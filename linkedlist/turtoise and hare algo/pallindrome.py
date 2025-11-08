# 234. Palindrome Linked List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        stack=[]

        temp=head

        while temp:
            stack.append(temp.val)
            temp=temp.next

        
        temp=head

        while temp:
            ele=stack.pop()
            if temp.val!=ele:
                return False
            temp=temp.next
        return True



# __________________________________________________________________________________________________

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        fast=head
        slow=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        

        if fast:
            slow=slow.next
        

        prev=None
        temp=slow

        while temp:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        

        first,second=head,prev
        while second:
            if first.val!=second.val:
                return False
            

            first=first.next
            second=second.next

        return True

        
            
              
   


    
          

        