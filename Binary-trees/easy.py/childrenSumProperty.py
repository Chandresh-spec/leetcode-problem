def sumchid(root):
    # Base case: empty node or leaf node
    if root is None or (root.left is None and root.right is None):
        return True

    # If both children exist
    if root.left and root.right:
        if root.data != root.left.data + root.right.data:
            return False

    # Recursively check left and right subtrees
    return sumchid(root.left) and sumchid(root.right)
