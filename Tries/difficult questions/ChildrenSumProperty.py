
# TufPlusLogo
# Runs left: 3
# User

# User
# Problem
# Editorial
# Submissions
# Discussion
# Notes
# AI
# Children Sum Property in Binary Tree


# 0

# 100
# Given the root of a binary tree, return true if and only if every node’s value is equal to the sum of the values stored in its left and right children.

# For any missing ( null ) child, its value is treated as 0.
# A leaf node automatically satisfies the rule because both children are null.

# Examples:
# Input: root = [1,4,3,5]

# Output: false

# Explanation:

# The root is 1, but its children sum to 4 + 3 = 7. Since 1 ≠ 7, the tree violates the property.
# Input: root = [10,4,6,1,3,2,4]

# Output: true

# Explanation:

# 4 = 1 + 3
# 6 = 2 + 4
# 10 = 4 + 6
# All internal nodes satisfy the condition.
# Input: root = [35,20,15,15,5,10,5]

# true
# false

# Submit
# Unlock Gamification Challenge
# Access comprehensive solutions, in-depth editorials, and additional learning resources.

# Upgrade to Plus
# Constraints:
# 1 ≤ n ≤ 104 (n = number of nodes `)

# -105 ≤ Node.val ≤ 105





# Children Sum Property in Binary Tree
# Completed



# We have been shipping at some speed!

# We know waiting isn't easy, and we are so grateful
# for your patience. Just a few more weeks, and we
# ship this as well.
# Thank you for understanding
# You are the best!
# Unlock Full Problem Insights
# Access comprehensive solutions, in-depth editorials, and additional learning resources.

# Upgrade to Plus




# No Submissions yet




# Comment
# Nothing to see here,
# start by adding your first question
# i_icon
# Click 'Save' — changes aren't auto-saved



# Save
# Hey Chandreshmoger! 👋
# Stuck on a problem? Ask me anything from logic to code, I’m here to guide you!

# FAQs BY USERS
# Explain the optimized approach for Children Sum Property in Binary Tree.
# What's the time and space complexity of Children Sum Property in Binary Tree?
# Can you dry-run the code for Children Sum Property in Binary Tree?
# Explain Children Sum Property in Binary Tree in simple terms.
# What are the edge cases to consider in Children Sum Property in Binary Tree?
# Explain Children Sum Property in Binary Tree with examples.
# Show me the brute-force approach to solve Children Sum Property in Binary Tree.
# Which data structures work best for Children Sum Property in Binary Tree?
# Compare Children Sum Property in Binary Tree with a similar problem.
# Ask your doubt
# 0 / 3,000

# Open AI Helper, drag to move









class Solution:
    def checkChildrenSum(self, root: TreeNode) -> int:
        # Your code goes here


        def helper(root):
            if not root:



            left_val=root.left.val if root.left else 0
            right_val=root.right.val if root.right else 0
        

            return (root.val==left_val+right_val and helper(root.left) and helper(root.right))
        

        return helper(root)
    

