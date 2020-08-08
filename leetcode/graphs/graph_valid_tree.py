# link: https://leetcode.com/problems/graph-valid-tree/


# union find solution
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # make set
        root = [x for x in range(n)]
        
        for e1,e2 in edges:
            root1 = self.findRoot(root, e1)
            root2 = self.findRoot(root, e2)
            if root1 == root2:
                return False
            
            root[root2]=root1
            
        return len(edges)==n-1
    
    def findRoot(self, root, i):
        while root[i]!=i:
            root[i]=root[root[i]]
            i=root[i]
        return i


# dfs solution
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # dfs in graph: make an adjacency list first
        if len(edges)!=n-1:
            return False
        al = {x:[] for x in range(n)}
        for e1,e2 in edges:
            al[e1].append(e2)
            al[e2].append(e1)
        
        def dfs(node):
            # print(al, node)
            neighbors = al.pop(node, [])
            for n in neighbors:
                dfs(n)
        dfs(0)
        # print(al,"h")
        return not al
        
                
         
        
                
            
        