# link: https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_width = 0
        res = collections.defaultdict(list)
        q = collections.deque()
        q.append([root, 0])
        while q:
            # print(q)
            # print(len(q))
            _, index = q[0]
            for _ in range(len(q)):
                node, c_index = q.popleft()
                if node.left:
                    q.append((node.left, 2*c_index))
                if node.right:
                    q.append((node.right, 2*c_index + 1 ))
            max_width = max(max_width, c_index - index +1)
        return max_width
        # print(res)