# [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        result = []
        level = 1
        current_level = 1
        temp_list = []
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [[root.val]]
        else:
            queue.append((root, level))
            result.append([root.val])
            while queue:
                root, level = queue.pop(0)
                if current_level == level:
                    temp_list.append(root.val)
                else:
                    temp_list = []
                    temp_list.append(root.val)
                    current_level = current_level + 1
                    result.append(temp_list)
                if root.left != None:
                    queue.append((root.left, level + 1))
                if root.right != None:
                    queue.append((root.right, level + 1))

            
        return result
