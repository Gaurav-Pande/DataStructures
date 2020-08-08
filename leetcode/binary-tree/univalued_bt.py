#link: https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s = set()
        s.add(root.val)
        self.dfs(root, s)
        return len(s)==1
        
    def dfs(self, root, s):
        if not root:
            return
        s.add(root.val)
        self.dfs(root.left, s)
        self.dfs(root.right, s)
        
        
    
