from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []

        queue = deque([(root, 0)])  # queue holds tuples: (node, horizontal_distance)
        hashmap = {}  # stores first node at each horizontal distance

        while queue:
            temp, x = queue.popleft()

            if x not in hashmap:
                hashmap[x] = temp.data  # store only the first node at each x

            if temp.left:
                queue.append((temp.left, x - 1))

            if temp.right:
                queue.append((temp.right, x + 1))

        # Extract top view from leftmost to rightmost horizontal distance
        lst = []
        for x in sorted(hashmap.keys()):
            lst.append(hashmap[x])

        return lst
