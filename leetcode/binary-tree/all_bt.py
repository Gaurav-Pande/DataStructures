# link: https://leetcode.com/problems/all-possible-full-binary-trees/submissions/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, N , memo = {}):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        # we atleast need 1 node or 3 node or 5 node
        # so we must increment the nodes by 2
        if N in memo:
            return memo[N]
        if N%2 == 0:
            return []
        res = []
        if N == 1:
            res.append(TreeNode(0))
            memo[N] = res
            return res
        i=1
        while i < N:
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-i-1)
            for nl in left:
                for nr in right:
                    root = TreeNode(0)
                    root.left = nl
                    root.right = nr
                    res.append(root)
                    memo[N] = res
            i+=2
                    
        return res
        
