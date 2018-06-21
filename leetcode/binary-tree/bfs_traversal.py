# [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import  collections
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





## A much better solution than above
class Solution2:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = collections.defaultdict(list)
        q = []
        res = []
        if root == None:
            return []
        else:
            q.append((root, 1))
            while q:
                ## Note pop(0) is a costly operation as we need to shift the rest of the value to one place left,
                ## so instead of that we could have used collections.Deque whihc offers faster insert and pop operation
                root, level = q.pop(0)
                dic[level].append(root.val)
                if root.left: q.append((root.left, level + 1))
                if root.right: q.append((root.right, level + 1))

        for key in sorted(dic, reverse=True):
            res.append(dic[key])

        return res




