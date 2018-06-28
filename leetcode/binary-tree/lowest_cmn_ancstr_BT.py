# Author: Gaurav Pande
# find the lowest common ancestor for given 2 nodes in a binary tree
# linke: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # the idea is you search the 2 nodes in a binary tree and check if both of the nodes are not None than root is
        # the answer else ch
        if root in (None, p, q):
            return root

        nodel = self.lowestCommonAncestor(root.left, p, q)
        noder = self.lowestCommonAncestor(root.right, p, q)
        if nodel and noder:
            return root
        else:
            return nodel or noder

if __name__  == '__main__':
    obj = TreeNode(3)
    obj.left = TreeNode(4)
    obj.right = TreeNode(2)
    obj.left.left = TreeNode(1)
    obj.left.left.left =  TreeNode(9)
    obj.left.right = TreeNode(6)
    p = obj.right.left = TreeNode(8)
    q = obj.right.right = TreeNode(7)
    ob = Solution()

    print(ob.lowestCommonAncestor(obj,p,q).val)