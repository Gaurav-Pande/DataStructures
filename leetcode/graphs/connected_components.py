# link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/


# Dfs
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(node,al, visited):
            # print(node)
            if visited[node]:
                return
            visited[node] = True
            for node in al[node]:
                    dfs(node,al,visited)
        al = {}
        for i in range(n):
            al[i] = []
        for edge in edges:
            source,target = edge[0],edge[1]
            al[source].append(target)
            al[target].append(source)
        count = 0
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                dfs(i,al,visited)
                count+=1        
        return count


# BFS solution
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        al = {i:[] for i in range(n)}
        for x,y in edges:
            al[x].append(y)
            al[y].append(x)
        print(al)
        count = 0
        visited = {x:False for x in range(n)}
        def bfs(node,al):
            q = collections.deque()
            q.append(node)
            for node in range(1,n): 
                while q:
                    cn = q.pop()
                    if not visited[cn]:
                        visited[cn]= True
                        for connected_nodes in al[cn]:
                            q.appendleft(connected_nodes)
                    else:
                        continue
        for node in range(n):
            if not visited[node]:
                bfs(node,al)
                count+=1
        return count



# Union find and path compression
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # make set:
        # make each element root of itself
        root = [x for x in range(n)]
        
        # go through the edges and find the root for each vertex on those eadge
        for edge in edges:
            root1 = self.findRoot(root, edge[0])
            root2 = self.findRoot(root, edge[1])
            
            # check if both of there root is same, if yes then they belong to the same set
            # otherwise do the union operation
            if root1 != root2:
                root[root2]=root1
                
        count = 0
        for i in range(n):
            if root[i]==i:
                count +=1
                
        print(root)
        return count
        
    def findRoot(self, root, i):
        # find the root/node which is the representative of the set containing node i
        # until the root of the node i is not iteself i, we are gonna make 
        while root[i] != i:
            # path compression
            root[i]=root[root[i]]
            i=root[i]
        return i
