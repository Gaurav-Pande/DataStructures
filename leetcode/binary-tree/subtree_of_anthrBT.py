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

