# https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors



class Solution(object):
    def cloneGraph(self, node):
        # datastructure to store graph
        d = {}
        # stack to track the path
        stack = [node]
        # to mark a node visited or not
        visited = []
        while stack:
            cn = stack.pop()
            if cn not in d:
                d[cn] = Node(cn.val, [])
            if cn in visited:
                continue
            visited.append(cn)
            for neighbor in cn.neighbors:
                if neighbor not in d:
                    d[neighbor] = Node(neighbor.val, [])
                d[cn].neighbors.append(d[neighbor])
                stack.append(neighbor)
        print(d)
        return d[node]




