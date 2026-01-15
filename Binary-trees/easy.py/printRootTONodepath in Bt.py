# rint root to node path in BT
# Medium

# Hints
# Company
# Given the root of a binary tree. Return all the root-to-leaf paths in the binary tree.



# A leaf node of a binary tree is the node which does not have a left and right child.


# Example 1

# Input : root = [1, 2, 3, null, 5, null, 4]

# Output : [ [1, 2, 5] , [1, 3, 4] ]

# Explanation : There are only two paths from root to leaf.

# From root 1 to 5 , 1 -> 2 -> 5.

# From root 1 to 4 , 1 -> 3 -> 4.



# Example 2

# Input : root = [1, 2, 3, 4, 5]

# Output : [ [1, 2, 4] , [1, 2, 5] , [1, 3] ]

# Explanation :



# Now your turn!

# Input : root = [1, 2, 3, 4, null, 5, 6, null, 7]



# Output:

# Pick your answer


# [ [1, 3, 4, 7], [1, 3, 5], [1, 3, 6] ]

# [ [1, 2, 4, 7], [1, 3, 6], [1, 2, 6] ]

# [ [1, 2, 4, 7], [1, 3, 5], [1, 3, 6] ]

# [ [1, 2, 4, 7], [1, 2, 4], [1, 3, 5]]
# Constraints

# 1 <= Number of Nodes <= 3*103
# -103 <= Node.val <= 103



# def helper(root, ds):
#     if not root:
#         return

#     ds.append(root.data)

#     if not root.left and not root.right:
#         ans.append(ds[:])
#     else:
#         helper(root.left, ds)
#         helper(root.right, ds)

#     ds.pop()




# node to Path

def helper(root, ds, target):
    if root is None:
        return False

    ds.append(root.data)

    if root.data == target:
        return True

    if helper(root.left, ds, target) or helper(root.right, ds, target):
        return True

    ds.pop()   # backtrack
    return False
