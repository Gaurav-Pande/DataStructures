# Author : Gaurav Pande
# Given a non empty binary search tree and a target value,find a value in the BST which is closest to the target value

class Solution(object):
    def closestValue(self, root, target):

        #Edge Case:
        if not root:
            return 0

        self.res = root.val
        #Process
        def dfs(root, target):
            if not root:
                return 0
            if abs(target - self.res) > abs(target - root.val):
                self.res = root.val
            if target > root.val:
                dfs(root.right, target)
            else:
                dfs(root.left, target)

        # Recursion
        dfs(root, target)
        return self.res