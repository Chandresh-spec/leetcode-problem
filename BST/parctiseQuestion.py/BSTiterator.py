# 653. Two Sum IV - Input is a BST
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:


# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105





class Solution:
    def findTarget(self, root,k):
        self.stack1 = []
        self.stack2 = []

        self.push_left(root)
        self.push_right(root)

        while self.stack1 and self.stack2 and self.stack1[-1] != self.stack2[-1]:
            v1 = self.stack1[-1].val
            v2 = self.stack2[-1].val

            if v1 + v2 == k:
                return True
            elif v1 + v2 < k:
                node = self.stack1.pop()
                if node.right:
                    self.push_left(node.right)
            else:
                node = self.stack2.pop()
                if node.left:
                    self.push_right(node.left)

        return False

    def push_left(self, node):
        while node:
            self.stack1.append(node)
            node = node.left

    def push_right(self, node):
        while node:
            self.stack2.append(node)
            node = node.right
