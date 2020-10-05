#link:  https://leetcode.com/problems/prison-cells-after-n-days/


class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        memo = {}
        cycle = False
        
        while N>0:
            if not cycle:
                state = tuple(cells)
                if state in memo:
                    # print(N, memo[state])
                    N = N%(memo[state]-N)
                    cycle = True
                else:
                    memo[state] = N
            # print(N)
            if N>0:
                N-=1
                next = self.nextday(cells)
                cells = next
        return cells
            
        
        
        
    def nextday(self, cells):
        temp = [0]
        for i in range(1,len(cells)-1):
            if cells[i-1] == cells[i+1]:
                temp.append(1)
            else:
                temp.append(0)
                
        temp.append(0)
        return temp
        
                
