# https://leetcode.com/problems/validate-binary-search-tree/submissions/


# the key idea is to block all unnecessary recursions.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    import sys

    def helper(self, root, lower=-sys.maxsize - 1, upper=sys.maxsize):
        if not root:
            return True

        if root.val <= lower or root.val >= upper:
            return False

        if not self.helper(root.right, root.val, upper):
            return False

        if not self.helper(root.left, lower, root.val):
            return False

        return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.helper(root)



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root)
    
    
    def isValid(self, root, lower = float('-inf'), higher = float('inf')):
        if not root:
            return True
        if not ( lower<root.val<higher):
            return False
        
        return self.isValid(root.left,lower,root.val) and self.isValid(root.right, root.val, higher)
        
        
        





