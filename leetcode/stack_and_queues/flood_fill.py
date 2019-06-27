# https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1393/

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        old_val = image[sr][sc]

        # self.bfs_traversal(sr, sc, newColor, image,old_val)
        self.dfs_traversal(sr, sc, newColor, image, old_val, [])
        return image

    def bfs_traversal(self, row, col, newColor, image, old_val):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        stack = []
        visited = []
        stack.append((row, col))
        image[row][col] = newColor
        while stack:
            cr, cc = stack.pop()
            for tr, tc in moves:
                nr = cr + tr
                nc = cc + tc
                if (nr, nc) != (row, col) and (nr, nc) not in visited:
                    if self.isvalid(nr, nc, image) and image[nr][nc] == old_val:
                        image[nr][nc] = newColor
                        visited.append((nr, nc))
                        stack.append((nr, nc))
        # print(image)

    def isvalid(self, row, col, image):
        if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]):
            return False
        else:
            return True

    def dfs_traversal(self, row, col, newColor, image, old_val, visited):
        if (row, col) not in visited:
            if self.isvalid(row, col, image) and image[row][col] == old_val:
                image[row][col] = newColor
                visited.append((row, col))
                self.dfs_traversal(row + 1, col, newColor, image, old_val, visited)
                self.dfs_traversal(row - 1, col, newColor, image, old_val, visited)
                self.dfs_traversal(row, col + 1, newColor, image, old_val, visited)
                self.dfs_traversal(row, col - 1, newColor, image, old_val, visited)


if __name__ == '__main__':
    ob = Solution()
    print(ob.floodFill(image=[[1,1,1],
                              [1,1,0],
                              [1,0,1]],sr=1,sc=1,newColor=2))