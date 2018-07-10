# Author: Gaurav Pande
# find the mode in a BST.
# link: https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

import collections
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = collections.defaultdict(int)
        self.morrisTraversal(root, d)
        if not d:
            return []
        # find the max element in the dictionary with values
        m = max(d.values())
        # now returns all keys having this m as its value
        return [k for k, v in d.items() if v == m]

    # The whole idea of morris traversal is to find a way back to the root node
    # after going left, that is what recursion does is it automatically using
    # stack push/pop find a way back to current node after traversing left child.
    # but to do it without recursion, we need to find the inorder predecessor of the
    # current node and link that predecessor to the current node.
    def morrisTraversal(self, root, d):
        if not root:
            return None

        current = root

        while current:
            # check to see if lef of current is none, if yes than print the current and
            # move to right subtree
            if not current.left:
                d[current.val] += 1
                current = current.right
            # if current has left child than we need to find the predecessor of the
            # current node
            else:
                pre = current.left
                # move to the right most element, that should be the predecessror of the
                # current node
                while pre.right and pre.right != current:
                    pre = pre.right

                # Now link this pre node to the current node, also remember if pre.right is not NOne yet
                # than that means we have already found the predecessor of the node
                if not pre.right:
                    pre.right = current
                    # lets move to left child as we have found the predecessor and linked it as well
                    current = current.left
                # revert or disable the link that we have formed during morris traversal
                else:
                    pre.right = None
                    d[current.val] += 1
                    current = current.right