# Author: Gaurav Pande
# find the mode in a BST.
# link: https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




##
## using dfs you traverse the tree, but we are using here extra space O(n)
##
import collections
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.d = collections.defaultdict(int)
        self.calMode(root)
        if not self.d:
            return []
        else:
            # find the max element in the dictionary with values
            m = max(self.d.values())
            # now returns all keys having this m as its value
            return [ k for k,v  in self.d.items() if v == m ]

    def calMode(self,root):
        if not root:
            return root
        self.d[root.val] += 1
        if root.left is not None:
            self.calMode(root.left)
        if root.right is not None:
            self.calMode(root.right)




# without using extra space:
class Solution(object):
    prev = None
    max_count = 0
    current_count = 0 
    result = []

    def findMode(self, root):
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        self.current_count = 1 if node.val != self.prev else self.current_count + 1
        if self.current_count == self.max_count:
            self.result.append(node.val)
        elif self.current_count > self.max_count:
            self.result = [node.val]
            self.max_count = self.current_count
        self.prev = node.val
        self.dfs(node.right)






