# link: https://leetcode.com/problems/find-all-the-lonely-nodes/

# find all lonely nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root.left and not root.right:
            return []
        result = []
        return self.dfs(root, result)
        
    def dfs(self, root, result):
        if not root:
            return
        if not root.left and root.right:
            result.append(root.right.val)
        if root.left and not root.right:
            result.append(root.left.val)
        self.dfs(root.left,result)
        self.dfs(root.right, result)
        return result
        
        