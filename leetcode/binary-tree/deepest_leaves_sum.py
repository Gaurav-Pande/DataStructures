# link: https://leetcode.com/problems/deepest-leaves-sum/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        track_sum = {}
        return self.dfs(root, 0, track_sum)
        
    def dfs(self, root,depth,track_sum):
        if not root:
            return
        if depth in track_sum:
            track_sum[depth] = track_sum[depth] + root.val
        else:
            track_sum[depth] = root.val
        self.dfs(root.left, depth+1,track_sum)
        self.dfs(root.right, depth+1, track_sum)
        return list(track_sum.items())[-1][1]
        
                
