# Author: Gaurav Pande
# find the paths in a bt which adds up to the target.
# link: https://leetcode.com/problems/path-sum-iii/description/

class Solution(object):
    def helper(self, root, target, so_far, cache):
        if root:
            complement = so_far + root.val - target
            if complement in cache:
                self.result += cache[complement]
            cache.setdefault(so_far+root.val, 0)
            cache[so_far+root.val] += 1
            self.helper(root.left, target, so_far+root.val, cache)
            self.helper(root.right, target, so_far+root.val, cache)
            cache[so_far+root.val] -= 1
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.pathSumHelper(root,sum, res, [])
        return res
    
    def pathSumHelper(self, root, target, res, temp):
        if not root:
            return
        if not root.left and not root.right and target-root.val == 0:
            # print(temp)
            temp.append(root.val)
            res.append(temp[:])
        else:
            self.pathSumHelper(root.left, target-root.val, res, temp+[root.val])
            self.pathSumHelper(root.right, target-root.val, res, temp + [root.val])
            

            