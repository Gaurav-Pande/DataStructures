# Author: Gaurav Pande
# check whether a given tree is a subtree of another tree
# link: https://leetcode.com/problems/subtree-of-another-tree/description/

# the solution is based on preorder traversal of the tree
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        l1 = self.preOrder(s, [])
        l2 = self.preOrder(t, [])
        print(l1, l2)
        if str(l2)[1:-1] in str(l1)[1:-1]:
            return True
        else:
            return False

    def preOrder(self, root, l):
        if not root:
            return None
        else:
            l.append('#' + str(root.val))
            if not root.left:
                l.append('ln')
            else:
                self.preOrder(root.left, l)
            if not root.right:
                l.append('Rn')
            else:
                self.preOrder(root.right, l)
        return l


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        ## for each node in s lets check if its subtree is equals to the t.
        if not t:
            return True
        if not s:
            return False
        if self.isIdentical(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    # below code is to check whether 2 trees are identical or not
    def isIdentical(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2:
            if root1.val == root2.val:
                return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)
            else:
                return False
        return False