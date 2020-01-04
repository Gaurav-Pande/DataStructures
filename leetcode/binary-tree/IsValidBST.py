# https://leetcode.com/problems/validate-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    import sys

    def helper(self, root, lower=-sys.maxsize - 1, upper=sys.maxsize):
        if not root:
            return True

        if root.val <= lower or root.val >= upper:
            return False

        if not self.helper(root.right, root.val, upper):
            return False

        if not self.helper(root.left, lower, root.val):
            return False

        return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.helper(root)







