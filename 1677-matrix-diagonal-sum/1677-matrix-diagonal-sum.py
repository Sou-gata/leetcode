class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            s += mat[i][i]
        for i in range(n):
            s += mat[i][n - i - 1]
        common = 0
        if (n - 1) % 2 == 0:
            i = (n - 1) // 2
            common = mat[i][i]
        return s - common