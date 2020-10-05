# link: https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target_node= len(graph)-1
        # source_node=0
        result = []
        def backtrack(curr_node, path):
            if curr_node == target_node:
                result.append(path[:])
                return
            
            else:
                for next_node in graph[curr_node]:
                    path.append(next_node)
                    backtrack(next_node, path)
                    # print(path)
                    path.pop()
                    
        backtrack(0,[0])
        return result
                
        
        