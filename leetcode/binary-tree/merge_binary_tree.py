# https://leetcode.com/problems/merge-two-binary-trees/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.mergeTree(t1, t2)

    def mergeTree(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTree(root1.left, root2.left)
        root1.right = self.mergeTree(root1.right, root2.right)
        return root1
