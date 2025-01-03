class Solution:
    def rotate(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        res = []
        for i in range(n):
            res.append([0] * n)
        for i in range(n):
            for j in range(n):
                res[n - j - 1][i] = mat[i][j]
        return res

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        n = len(mat)
        t = self.rotate(mat)
        for i in range(3):
            if t == target:
                return True
            if i != 2:
                t = self.rotate(t)
        return False