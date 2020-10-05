#link: https://leetcode.com/problems/critical-connections-in-a-network/

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        
        adj = collections.defaultdict(list)
        
        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)
            
        
        visited = [False for i in range(n)]
        lr = [i for i in range(n)]
        cr = 0
        pn = -1
        cn=0
        res =[]
        
        def dfs(graph, res, visited, cn, pn, cr, lr):
            visited[cn] = True
            lr[cn] = cr
            for nextnode in graph[cn]:
                if nextnode == pn:
                    continue
                if not visited[nextnode]:
                    dfs(graph, res, visited,nextnode, cn, cr + 1, lr)
                lr[cn] = min(lr[cn], lr[nextnode])
                if cr +1 <= lr[nextnode]:
                    res.append([cn,nextnode])
                    
        dfs(adj,res, visited, cn, pn, cr , lr)
        return res