# link: https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # max_sum = float('-inf')
        self.maxSum(root)
        return self.max_sum
    
    def maxSum(self, node):
        if not node:
            return 0
        left = max(self.maxSum(node.left),0)
        right = max(self.maxSum(node.right),0)
        curr_sum = node.val + left + right
        self.max_sum = max(self.max_sum, curr_sum)
        return node.val+max(left,right)
        
        