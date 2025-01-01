class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        squares = [
            [grid[0][0], grid[0][1], grid[1][0], grid[1][1]],
            [grid[0][1], grid[0][2], grid[1][1], grid[1][2]],
            [grid[1][0] ,grid[1][1], grid[2][0], grid[2][1]],
            [grid[1][1] ,grid[1][2], grid[2][1], grid[2][2]],
        ]
        for square in squares:
            if square.count("B") != 2:
                return True
        return False