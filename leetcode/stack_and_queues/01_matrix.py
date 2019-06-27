# https://leetcode.com/problems/01-matrix/
import collections
class Solution:
    def updateMatrix(self, matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])
        r = 0
        result = row_len * [col_len * [0]]
        q = collections.deque()
        while r < row_len:
            c = 0
            while c < col_len:
                if matrix[r][c] == 0:
                    q.append((r, c))
                else:
                    matrix[r][c] = 10000
                c += 1
            r += 1
        #self.dfs(0,0,matrix)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            tr, tc = q.popleft()
            for r, c in moves:
                nr = tr + r
                nc = tc + c
                if self.isValid(nr, nc, matrix):
                    if matrix[nr][nc] <= matrix[tr][tc] + 1:
                        continue
                    q.append((nr, nc))
                    matrix[nr][nc] = matrix[tr][tc] + 1

        return matrix

    def isValid(self, r, c, matrix):
        if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]):
            return False
        else:
            return True

    # def dfs(self,row,col,matrix):
    #     if self.isValid(row,col,matrix):
    #         if matrix[row][col] > matrix[row][col] +1:
    #             matrix[row][col] = matrix[row][col] + 1
    #             self.dfs(row+1,col,matrix)
    #             self.dfs(row-1,col,matrix)
    #             self.dfs(row,col+1,matrix)
    #             self.dfs(row,col-1,matrix)


if __name__ == '__main__':
    ob = Solution()
    print(ob.updateMatrix(matrix= [[0,0,0],
 [0,1,0],
 [1,1,1]]))





jagurush