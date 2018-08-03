# Author: Gaurav Pande
#link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        dic = collections.defaultdict(list)
        q = []
        res = []
        if root == None:
            return []
        else:
            q.append((root, 1))
            while q:
                root, level = q.pop(0)
                dic[level].append(root.val)
                if root.left: q.append((root.left, level + 1))
                if root.right: q.append((root.right, level + 1))

        for key in sorted(dic, reverse=True):
            res.append(dic[key])

        return res

