# link: https://leetcode.com/problems/delete-node-in-a-bst/submissions/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # we have found the node to be deleted:
            if not root.left and not root.right:
                root = None
            # node is not leaf and it has right chile
            # we need to find th successor and recursively delete it
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
                
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
    
    def successor(self, root):
        # one step right and all the way left
        
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val