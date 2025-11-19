# 61. Rotate List
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(head,k):
        if head is None:
            return None
        if head.next is None:
            return head

        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        

        k=k%count
        if k==0:
            return head
        fast=head
        slow=head
        for i in range(k):
            fast=fast.next
        

        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        
        
        head_node=slow.next
        slow.next=None
        fast.next=head
        head=head_node

        return head
