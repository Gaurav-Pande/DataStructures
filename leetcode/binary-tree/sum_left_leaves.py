# author: Gaurav pande
# find the sum of all the left leaves in a bt
# link: https://leetcode.com/problems/sum-of-left-leaves/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            # check if root.left is not none and also if it is leave
            if root.left and not root.left.left and not root.left.right:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else:
                # if not leave than check the same for the left and right child
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        else:
            return 0