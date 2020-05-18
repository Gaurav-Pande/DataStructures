# link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3293/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		#####
		## The idea is to calculate height of left and right subtree and add 2 to it
		## and return maximum of it.
		##
		#####

		def dfs(root):
			if not root:
				return -1
			else:
				lh = dfs(root.left)
				rh = dfs(root.right)
				result.append(lh + rh + 2)
			return 1 + max(lh, rh)

		if not root:
			return 0
		result = []
		dfs(root)
		return max(result)

