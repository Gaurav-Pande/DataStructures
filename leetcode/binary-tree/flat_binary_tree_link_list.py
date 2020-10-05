# link:https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # do a preorder traversal and then link back the edges
        
        self.preorder(root)
        
        
    def preorder(self,root):
        if not root:
            return 
        if not root.left and not root.right:
            return root
        
        left = self.preorder(root.left)
        right = self.preorder(root.right)
        
        # if left: print("l",left.val, root.val)
        # if right: print(right.val)
        
        # left = 3
        # root = 2
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None
            
        if right:
            return right
        else:
            return left
            
        
        
        
        
        
        
        