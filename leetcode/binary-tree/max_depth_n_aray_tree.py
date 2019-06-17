# https://leetcode.com/problems/maximum-depth-of-n-ary-tree

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int


        """
        # Recursive or DFS Solution
        # if not root:
        #     return 0
        # elif not root.children:
        #     return 1
        # else:
        #     return max(self.maxDepth(r) for r in root.children) + 1

        # BFS solution
        if not root:
            return 0
        import collections
        q = collections.deque()
        depth = 0
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                for elem in node.children:
                    q.append(elem)
            depth += 1
        return depth
