# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB) :
        hashmap={}
        temp=headA

        while temp:
            hashmap[temp]=1
            temp=temp.next
        

        temp=headB

        while temp:
            if temp in hashmap:
                return temp
            temp=temp.next
        

        return None
        
        
        



        