class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy = 0
        xz = 0
        yz = 0
        for i in range(n):
            mx = grid[i][0]
            for j in range(n):
                if grid[i][j] > 0:
                    xy += 1
                if grid[i][j] > mx:
                    mx = grid[i][j]
            xz += mx
        for col in zip(*grid):
            yz += max(col)
        return xy + xz + yz
