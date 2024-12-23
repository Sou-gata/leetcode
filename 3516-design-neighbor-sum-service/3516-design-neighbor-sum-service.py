class NeighborSum:
    
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.l = len(grid)

    def findLocation(self, value: int) -> list[int]:
        for i in range(self.l):
            for j in range(self.l):
                if self.grid[i][j] == value:
                    return [i, j]

    def adjacentSum(self, value: int) -> int:
        s = 0
        [posR, posC] = self.findLocation(value)
        # vertical
        if posR == 0:
            s += self.grid[posR + 1][posC]
        elif posR == self.l - 1:
            s += self.grid[posR - 1][posC]
        else:
            s += self.grid[posR + 1][posC] + self.grid[posR - 1][posC]
        # horizontal
        if posC == 0:
            s += self.grid[posR][posC + 1]
        elif posC == self.l - 1:
            s += self.grid[posR][posC - 1]
        else:
            s += self.grid[posR][posC + 1] + self.grid[posR][posC - 1]
        return s

    def diagonalSum(self, value: int) -> int:
        s = 0
        [posR, posC] = self.findLocation(value)
        dig = {
            "tl": [posR - 1, posC - 1],
            "tr": [posR - 1, posC + 1],
            "bl": [posR + 1, posC - 1],
            "br": [posR + 1, posC + 1]
        }
        a = []
        for i in dig.keys():
            if dig[i][0] < 0 or dig[i][0] > self.l - 1 or dig[i][1] < 0 or dig[i][1] > self.l - 1:
                continue
            else:
                a.append(i)
        for i in a:
            v = dig[i]
            s += self.grid[v[0]][v[1]]
        return s


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)