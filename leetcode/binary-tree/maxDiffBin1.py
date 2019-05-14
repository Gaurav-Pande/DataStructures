# find the max difference betweena  node and its ancestor in a binary tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max = 0
        self.min = 10000

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findMaxDiff(root)
        return self.max

    # def findMaxDiff(self, root, mn, mx):
    #     if not root:
    #         return mx - mn
    #     mx = max(mx, root.val)
    #     mn = min(mn, root.val)
    #     print(mx, mn)
    #     a = self.findMaxDiff(root.left, mn, mx)
    #     b = self.findMaxDiff(root.right, mn, mx)
    #     print(a, b, max(a, b))
    #     return max(a, b)

    def findMaxDiff(self,root):
        if not root:
            return 10000
        if not root.left and not root.right:
            return root.val
        val = min(self.findMaxDiff(root.left),self.findMaxDiff(root.right))
        print(val)
        diff = abs(root.val-val)
        self.max = max(self.max, diff)
        print(self.max)
        return min(root.val,val)









