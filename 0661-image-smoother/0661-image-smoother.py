class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans = []
        for i in range(m):
            ans.append([-1] * n)
        for i in range(m):
            for j in range(n):
                (t, n1) = (0, 0) if i == 0 else (img[i - 1][j], 1)
                (b, n2) = (0, 0) if i == m - 1 else (img[i + 1][j], 1)
                (l, n3) = (0, 0) if j == 0 else (img[i][j - 1], 1)
                (r, n4) = (0, 0) if j == n - 1 else (img[i][j + 1], 1)
                (tl, n5) = (0, 0) if i - 1 < 0 or j - 1 < 0 else (img[i - 1][j - 1], 1)
                (tr, n6) = (0, 0) if i - 1 < 0 or j + 1 > n - 1 else (img[i - 1][j + 1], 1)
                (bl, n7) = (0, 0) if i + 1 > m - 1 or j - 1 < 0 else (img[i + 1][j - 1], 1)
                (br, n8) = (0, 0) if i + 1 > m - 1 or j + 1 > n - 1 else (img[i + 1][j + 1], 1)
                avg = (t + b + l + r + tl + tr + bl + br + img[i][j]) // (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + 1)
                ans[i][j] = avg
        return ans