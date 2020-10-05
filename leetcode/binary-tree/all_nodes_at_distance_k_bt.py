# link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(node, parent = None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root)
        
        q = collections.deque([(target, 0)])
        
        visited = set()
        visited.add(target)
        
        while q:
            if q[0][1] == K:
                return [ node.val for node, d in q]
            node, d = q.popleft()
            for neighbor in (node.left, node.right, node.parent):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor,d+1))
                    
        return []
