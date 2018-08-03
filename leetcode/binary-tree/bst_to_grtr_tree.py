# Author: Gaurav Pande
# convert a BST to greater bst
# link: https://leetcode.com/problems/convert-bst-to-greater-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# The solution is based on the reverse inorder traversal as we will have to visit the greated value nodes in the Bst
# and keep adding their sum and changing the value of the root witht that sum. so we need to visit the right subtree
# first and the than root(change its value) and than left subtree.

class Solution:
    def __init__(self):
        self.sum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST(root.right)
            self.sum += root.val
            root.val = self.sum
            self.convertBST(root.left)
        return root


# using morris traversal, finding predecessor