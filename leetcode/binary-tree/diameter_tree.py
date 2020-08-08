#link: https://leetcode.com/problems/tree-diameter/

class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        self.graph = collections.defaultdict(list)
        self.diameter = 0
        for x,y in edges:
            self.graph[x].append(y)
            self.graph[y].append(x)
        self.v = len(self.graph)
        visited = [False]*self.v
        far, dist  = self.dfs(0, visited)
        last, res = self.dfs(far,visited)
        return res
    
    def dfs(self, node, visited):
        visited[node]=True
        dist = 0
        current = node
        for c in self.graph[node]:
            if not visited[c]:
                cn, cd = self.dfs(c, visited)
                if cd +1 > dist:
                    dist = cd+1
                    current = cn
                    
        visited[node]=False
        return current, dist
                    
        
        