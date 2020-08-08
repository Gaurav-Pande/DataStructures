# link: https://leetcode.com/problems/course-schedule/

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = collections.defaultdict(list)
        self.v = numCourses
        for x,y in prerequisites:
            self.graph[y].append(x)
            
        if not self.detectCycle():
            return True
        else:
            return False
        
    def detectCycle(self):
        stack = [False]*self.v
        visited = [False]*self.v
        for node in range(self.v):
            if not visited[node]:
                if self.dfs(node, stack, visited):
                    return True
        return False
    
    def dfs(self, node, stack, visited):
        stack[node]=True
        visited[node]=True
        for children in self.graph[node]:
            if stack[children]:
                return True
            if not visited[children]:
                if self.dfs(children, stack, visited):
                    return True
        stack[node]=False
        return False
