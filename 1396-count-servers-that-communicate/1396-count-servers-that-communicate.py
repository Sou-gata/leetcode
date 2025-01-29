class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        row_counts = [0] * n
        col_counts = [0] * m
        k = 0
        for row in grid:
            row_counts[k] = row.count(1)
            k += 1
        k = 0
        for col in zip(*grid):
            col_counts[k] = col.count(1)
            k += 1
        count = 0
        for i in range(n):
            for j in range(m):
                if (row_counts[i] > 1 or col_counts[j] > 1) and grid[i][j] == 1:
                    count += 1
        return count