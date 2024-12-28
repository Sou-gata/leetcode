class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 or n == 1:
            return True
        for i in range(n - 1):
            l = matrix[0][i]
            for j in range(1, min(m, n)):
                if i + j < n and matrix[j][i + j] != l:
                    return False
        for i in range(1, m - 1):
            l = matrix[i][0]
            for j in range(1, min(m, n)):
                if i + j < m and matrix[i + j][j] != l:
                    return False
        return True