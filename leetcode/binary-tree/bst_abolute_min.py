# https://leetcode.com/problems/minimum-absolute-difference-in-bst/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # inorder traversal and than first 2 number
        l = []

        def dfs(root):
            if root.left:
                dfs(root.left)
            l.append(root.val)
            if root.right:
                dfs(root.right)

        dfs(root)

        def min_val(a):
            return min(abs(a - b) for a, b in zip(a, a[1:]))

        return min_val(l)





