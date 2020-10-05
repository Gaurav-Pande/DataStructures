#link: https://leetcode.com/problems/kill-process/solution/


class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        # brute force method
        """
        pid =  [1, 3, 10, 5]
        ppid = [3, 0, 5, 3]
        kill = 5
        Output: [5,10]
           3
         /   \
        1     5
             /
            10
        Kill 5 will also kill 10.
        """
        # for 5 we search 5 in ppid and get the index 2 which will point ot its child in pid
        #we get 10, then again we search in ppid but we do not find it so that is the lead
        # so end up deleting 5 and 10
        if kill == 0:
            return []
        self.result = []
        self.recursion(pid,ppid,kill, [])
        return self.result[:-1]
       
    
    def recursion(self, pid, ppid, kill,temp): 
        self.result.append(kill)
        for i in range(len(ppid)):
            if ppid[i] == kill:
                self.result.append(self.recursion(pid, ppid, pid[i], temp))
        
      

# Simple bfs approach

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        # brute force method
        """
        pid =  [1, 3, 10, 5]
        ppid = [3, 0, 5, 3]
        kill = 5
        Output: [5,10]
           3
         /   \
        1     5
             /
            10
        Kill 5 will also kill 10.
        """
        # for 5 we search 5 in ppid and get the index 2 which will point ot its child in pid
        #we get 10, then again we search in ppid but we do not find it so that is the lead
        # so end up deleting 5 and 10
        result =[]
        dic = collections.defaultdict(list)
        for c,p in zip(pid,ppid):
            dic[p].append(c)
        # print(dic)
        stack = [kill]
        while stack:
            tokill = stack.pop()
            result.append(tokill)
            stack.extend(dic[tokill])
            
        return result
            
        
        
        
        
 # dfs approach       
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        # brute force method
        """
        pid =  [1, 3, 10, 5]
        ppid = [3, 0, 5, 3]
        kill = 5
        Output: [5,10]
           3
         /   \
        1     5
             /
            10
        Kill 5 will also kill 10.
        """
        # for 5 we search 5 in ppid and get the index 2 which will point ot its child in pid
        #we get 10, then again we search in ppid but we do not find it so that is the lead
        # so end up deleting 5 and 10
        result =[]
        dic = collections.defaultdict(list)
        for c,p in zip(pid,ppid):
            dic[p].append(c)
        def dfs(kill):
            result.append(kill)
            for children in dic[kill]:
                dfs(children)
            
        dfs(kill)
        return result
        
        
        
    
    
            
        
        
        
        
        

        
        
        
