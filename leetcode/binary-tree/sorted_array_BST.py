# Author: Gaurav Pande
# convert a sorted array to height balanced bSt
# link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, nums, start, end):
        if start > end:
            return None
        mid = int((start + end) / 2)
        root = TreeNode(nums[mid])
        root.left = self.buildTree(nums, start, mid - 1)
        root.right = self.buildTree(nums, mid + 1, end)

        return root








