class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        result = []
        for i in range(m):
            result.append([0] * n)
        for i in indices:
            for j in range(n):
                result[i[0]][j] += 1
            for j in range(m):
                result[j][i[1]] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if result[i][j] % 2 == 1:
                    count += 1
        return count