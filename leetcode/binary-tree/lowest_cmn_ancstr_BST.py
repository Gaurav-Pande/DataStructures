# Author: Gaurav Pande
# find the lowest common ancestor for a given 2 nodes in a binary search tree
# link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # The idea is very simple here, if p and q belongs to same subtree than (root.val - p.val) * (root.val - q.val)
        # should be positive, else both belongs to different sub tree and root is the LCA. If both belong to same sub
        # tree than we traverse the list untill one is root and other is on either left or right subtree.
        while (root.val - p.val) * (root.val - q.val) > 0:
            if p.val < root.val:
                root = root.left
            else:
                root = root.right
        return root


    def lowestCommonAncestorII(self, root, p, q):
        while root:
            if root.val > max(p.val,q.val):
                root = root.left
            elif root.val < min(p.val,q.val):
                root = root.right
            else:
                return root
        return root




    # Recursive solution
    def lowestCommonAncestorIII(self, root, p, q):
        if not root or not p or not q:
            return None

        if root.val > max(p.val,q.val):
            return self.lowestCommonAncestorIII(root.left,p,q)
        elif root.val < min(p.val,q.val):
            return self.lowestCommonAncestorIII(root.right,p,q)

        return root




