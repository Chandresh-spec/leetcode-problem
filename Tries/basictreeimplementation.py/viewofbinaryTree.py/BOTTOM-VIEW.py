from collections import deque

class Solution:
    def bottomView(self, root):
        if not root:
            return []

        queue = deque([(root, 0)])  # (node, horizontal distance)
        hashmap = {}  # stores x: bottom-most node.data

        while queue:
            temp, x = queue.popleft()

            # Always update hashmap for bottom view
            hashmap[x] = temp.data

            if temp.left:
                queue.append((temp.left, x - 1))
            if temp.right:
                queue.append((temp.right, x + 1))

        # Collect values from leftmost to rightmost horizontal level
        lst = []
        for x in sorted(hashmap.keys()):
            lst.append(hashmap[x])

        return lst
