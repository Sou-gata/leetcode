class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row_min = [0] * m
        for i in range(m):
            row_min[i] = min(matrix[i])
        col_max = [0] * n
        for i in range(n):
            ma = matrix[0][i]
            for j in range(1, m):
                if matrix[j][i] > ma:
                    ma = matrix[j][i]
            col_max[i] = ma
        for i in col_max:
            if i in row_min:
                return [i]
        return []