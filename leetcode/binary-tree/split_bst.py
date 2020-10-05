# link:https://leetcode.com/problems/split-bst/discuss/113799/Python-straightforward-recursive-solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [None, None]
        
        if root.val == V:
            temp = root.right
            root.right = None
            return [root, temp]
        
        if root.val < V:
            left, right = self.splitBST(root.right, V)
            root.right = left
            return [root, right]
        else:
            left, right = self.splitBST(root.left, V)
            root.left = right
            return [left, root]
            