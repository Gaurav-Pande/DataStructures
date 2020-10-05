#link: https://leetcode.com/problems/maximum-average-subtree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        
        def dfs(root, sum, num):
            if not root:
                return [0,0]
            sum = root.val
            num = 1
            ls, ln = dfs(root.left, sum, num)
            rs, rn = dfs(root.right, sum, num)
            sum += ls+rs
            num += ln+rn
            # print(sum,num)
            self.res = max(self.res, float(sum)/float(num))
            # print(self.res)
            return [sum, num]
        self.res = 0
        sum = 0
        num = 0   
        dfs(root, sum, num)
        return self.res
        