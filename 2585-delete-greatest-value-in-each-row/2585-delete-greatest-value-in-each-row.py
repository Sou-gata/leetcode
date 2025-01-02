class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        s = 0
        for col in zip(*grid):
            s += max(col)
        return s