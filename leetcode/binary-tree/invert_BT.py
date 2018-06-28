# Author: Gaurav Pande
# invert a binary tree
# link: https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    # Recursive Solution DFS
    # Here we are swapping at the end recursion call
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

    # Recursive Solution DFS
    # here we will swap before the recursion call
    def invertTreeII(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


    # Iterative Solution based on BFS traversal
    # here we go level by level swap the nodes and add their childrens to queue
    def invertTreeIII(self,root):
        q = collections.deque()
        if not root:
            return None
        q.append(root)
        while q:
            elem = q.popleft()
            # swap left and right nodes
            temp = elem.right
            elem.right = elem.left
            elem.left = temp
            if elem.right:
                q.append(elem.right)
            if elem.left:
                q.append(elem.left)
        return root
