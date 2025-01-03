class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        mx = 0
        r = 0
        for i, row in enumerate(mat):
            s = row.count(1)
            if s > mx:
                mx = s
                r = i
        return [r, mx]