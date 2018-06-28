# Author: Gaurav Pande
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
# the path equals the given sum.
# link: https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        if root.left == None and root.right == None and sum - root.val == 0:
            return True

        else:
            sum -= root.val

            return self.hasPathSum(root.left,sum) and self.hasPathSum(root.right,sum)

# The below solution is based on if you think from preorder perspective
class SolutionPreorder:
    def __init__(self):
        self.result = False
    def hasPathSum(self,root,sum):
        if root == None:
            return False
        self.preorder(root,0,sum)
        return self.result

    def preorder(self,root,c_sum,sum):

        c_sum += root.val

        if root.left == None and root.right == None and c_sum == sum:
            self.result = True

        if root.left != None:
            self.preorder(root.left, c_sum, sum)

        if root.right != None:
            self.preorder(root.right,c_sum,sum)






if __name__  == '__main__':
    obj = TreeNode(1)
    obj.left = TreeNode(1)
    obj.right = TreeNode(1)
    obj.left.left = TreeNode(1)
    obj.left.right = TreeNode(1)
    obj.right.left = TreeNode(1)
    obj.right.right = TreeNode(1)

    ob = Solution()

    print(ob.hasPathSum(obj,3))



