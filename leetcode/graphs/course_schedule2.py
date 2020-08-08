# link: https://leetcode.com/problems/course-schedule-ii/submissions/

'''
In this you have to detect the cycle, if there is cycle then return []
else, return the topological sorting of the graph
'''

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # in this question we have to print the topological order but also detect the cycle
        self.graph = collections.defaultdict(list)
        self.v = numCourses
        for x,y in prerequisites:
            self.graph[y].append(x)
        
        iscycle, topo =  self.detectCycle()
        if iscycle:
            return []
        else:
            return topo
    
    def detectCycle(self):
        stack, visited = [False]*self.v, [False]*self.v
        topo = []
        for node in range(self.v):
            if not visited[node]:
                if self.dfs(node, stack, visited, topo):
                    return True, []
        return False, topo
    
    
    def dfs(self,node, stack, visited, topo):
        visited[node]=True
        stack[node]=True
        for children in self.graph[node]:
            if stack[children]:
                return True
            if not visited[children]:
                if self.dfs(children, stack, visited, topo):
                    return True
        stack[node]=False
        topo.insert(0,node)
        return False
