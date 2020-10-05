#link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/solution/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes_list = []
        
        def dfs(root, r ,c):
            if not root:
                return None
            nodes_list.append([c, r , root.val])
            dfs(root.left, r+1, c-1)
            dfs(root.right, r+1, c+1)
            
            
        def bfs(root):
            q = collections.deque()
            q.append([root,0,0])
            while q:
                node, r, c = q.popleft()
                if node:
                    nodes_list.append([c,r,node.val])
                    q.append([node.left,r+1,c-1])
                    q.append([node.right,r+1,c+1])
                    
        # bfs(root)
        dfs(root,0,0)
        nodes_list.sort()
        # print(nodes_list)
        result = collections.OrderedDict()
        for c, r, v in nodes_list:
            if c in result:
                result[c].append(v)
            else:
                result[c] = [v]
        
        return result.values()