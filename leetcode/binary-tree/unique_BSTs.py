# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        return self.calculate(1, n)

    def calculate(self, start, end):
        result = []

        if start > end:
            result.append(None)
            return result

        for i in range(start, end + 1):
            leftsubtree = self.calculate(start, i - 1)
            rightsubtree = self.calculate(i + 1, end)
            for j in range(len(leftsubtree)):
                for k in range(len(rightsubtree)):
                    root = TreeNode(i)
                    root.left = leftsubtree[j]
                    root.right = rightsubtree[k]
                    result.append(root)
        return result
