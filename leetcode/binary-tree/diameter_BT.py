# Author: Gaurav Pande
# calculate the diameter of the binary tree,ie the longest path between any two nodes
# link:

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.result = []
        self.traverseDfs(root)
        return max(self.result)
    ## The idea is simple: we calculate height of the left subtree and height of the right subtree and add
    # those 2 heights +2(+2 to count left edge and right of the root) will give the longest path in the tree
    def traverseDfs(self,root):
        if not root:
            return -1
        ld  = self.traverseDfs(root.left)
        rd = self.traverseDfs(root.right)
        self.result.append(ld + rd + 2)
        return 1 + max(ld,rd)