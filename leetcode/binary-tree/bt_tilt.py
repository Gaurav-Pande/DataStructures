# Author: Gaurav Pande
"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.
"""

# link: https://leetcode.com/problems/binary-tree-tilt/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.Traverse(root)
        return self.sum

    def Traverse(self, root):
        if not root:
            return 0
        left = self.Traverse(root.left)
        right = self.Traverse(root.right)
        self.sum += abs(left - right)
        return left + right + root.val

