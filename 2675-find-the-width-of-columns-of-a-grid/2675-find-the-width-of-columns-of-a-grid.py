class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * len(grid[0])
        i = 0
        for col in zip(*grid):
            ans[i] = max([len(str(i)) for i in col])
            i += 1
        return ans