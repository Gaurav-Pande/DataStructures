# link: https://leetcode.com/problems/friend-circles/

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # first create a adjacancy list
        nodes= len(M)
        visited = [0]*nodes
        result=0
        for node in range(nodes):
            if visited[node] == 0:
                self.dfs(M,node,visited)
                result+=1
        
        return result
    
    def dfs(self,M,node,visited):
        for j in range(len(M)):
            if M[node][j] == 1 and visited[j]==0:
                visited[j]=1
                self.dfs(M,j,visited)
                
                
                
