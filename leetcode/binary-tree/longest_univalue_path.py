# link: https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        self.dfs(root)
        
        return self.res
    
    
    def dfs(self,root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        l1,r1=0,0
        if root.left and root.left.val == root.val:
            l1 = l + 1
        if root.right and root.right.val == root.val:
            r1 = r +1
            
        self.res = max(self.res, l1+r1)
        return max(l1,r1)
    
