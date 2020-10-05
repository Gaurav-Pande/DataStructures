#link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        # print(res)
        return res[k-1]
            
            
