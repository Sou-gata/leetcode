class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix[0])
        ans = [] + matrix
        col_max = [0] * n
        k = 0
        for col in zip(*matrix):
            col_max[k] = max(col)
            k += 1
        for i in range(len(matrix)):
            for j in range(n):
                if ans[i][j] == -1:
                    ans[i][j] = col_max[j]
        return ans