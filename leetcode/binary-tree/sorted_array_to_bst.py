# link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.BST(0, len(nums)-1, nums)
    
    def BST(self, left, right, nums):
        if left>right:
            return None
        middle = (left+right)//2
        if (left+right)%2:
            middle+=1
        root = TreeNode(nums[middle])
        root.left = self.BST(left,middle-1, nums)
        root.right = self.BST(middle+1, right, nums)
        return root
        
        