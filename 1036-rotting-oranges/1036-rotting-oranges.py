from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, freshCount = 0, 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    freshCount += 1
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and freshCount > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for d in dir:
                    row = d[0] + i
                    col = d[1] + j
                    if (row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    freshCount -= 1
            time += 1
        return time if freshCount == 0 else -1