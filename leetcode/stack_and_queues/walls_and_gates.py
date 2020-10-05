# link: https://leetcode.com/problems/walls-and-gates/

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        '''
        Instead of searching from an empty room to the gates, how about searching the other way round? In other words, we initiate breadth-first search (BFS) from all gates at the same time. Since BFS guarantees that we search all rooms of distance d before searching rooms of distance d + 1, the distance to an empty room must be the shortest.
        '''
        if not rooms:
            return 
        rows, cols = len(rooms), len(rooms[0])
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    
                    
        while q:
            cr, cc = q.popleft()
            for mr,mc in moves:
                nr,nc = mr + cr, mc + cc
                if self.isvalid(rooms, nr, nc) and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[cr][cc] + 1
                    q.append((nr,nc))
                    
                    
    def isvalid(self, rooms, r, c):
        rows, cols = len(rooms), len(rooms[0])
        if r<0 or c<0 or r >= rows or c >= cols:
            return False
        return True