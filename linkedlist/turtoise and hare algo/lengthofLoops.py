# Length of loop in LL


# 0

# 100
# Medium

# Hints
# Given the head of a singly linked list, find the length of the loop in the linked list if it exists. Return the length of the loop if it exists; otherwise, return 0.



# A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos is used to denote the index (0-based) of the node from where the loop starts.



# Note that pos is not passed as a parameter.


# Examples:


# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1

# Output: 4

# Explanation: 2 -> 3 -> 4 -> 5 - >2, length of loop = 4.



# Input: head -> 1 -> 3 -> 7 -> 4, pos = -1

# Output: 0

# Explanation: No loop is present in the linked list.





# Input: head -> 6 -> 3 -> 7, pos = 0




# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        # class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None


        slow=head
        fast=head

        while fast and fast.next:
            
            fast=fast.next.next
            slow=slow.next

            if slow==fast:
                break
        else:
            return 0
        slow=head
        cnt=0
        while fast!=slow:
            cnt+=1
            slow=slow.next
        
        return cnt


