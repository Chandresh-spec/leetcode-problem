class Solution:
    def floorCeilOfBST(self, root, key):
        floor = ceil = -1
        temp = root

        while temp:
            if temp.data == key:
                return [key, key]

            if temp.data < key:
                floor = temp.data
                temp = temp.right
            else:
                ceil = temp.data
                temp = temp.left

        return [floor, ceil]
