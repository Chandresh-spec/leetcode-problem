class Solution:
    def succPredBST(self, root, key):
        pred = -1
        succ = -1
        curr = root

        # Step 1: search for key while tracking floor/ceil
        while curr:
            if curr.data < key:
                pred = curr.data
                curr = curr.right
            elif curr.data > key:
                succ = curr.data
                curr = curr.left
            else:
                break

        # Step 2: if key found, refine using subtrees
        if curr:
            # predecessor = max in left subtree
            temp = curr.left
            while temp:
                pred = temp.data
                temp = temp.right

            # successor = min in right subtree
            temp = curr.right
            while temp:
                succ = temp.data
                temp = temp.left

        return [pred, succ]
