# Author: Gaurav Pande
# find the paths in a bt which adds up to the target.
# link: https://leetcode.com/problems/path-sum-iii/description/

# bruteforce solution
# time complexity: O(n^2) or O(nlogn)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        else:
            return 0

    def findPath(self, root, target):
        if root:
            return int(root.val == target) + self.findPath(root.left, target - root.val) + self.findPath(root.right,
                                                                                                         target - root.val)
        else:
            return 0
