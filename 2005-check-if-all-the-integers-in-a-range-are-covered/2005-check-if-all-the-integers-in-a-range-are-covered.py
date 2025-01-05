class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = True
        for i in range(left, right + 1):
            c = False
            for l, r in ranges:
                if l <= i <= r:
                    c = True
                    break
            covered = covered and c
        return covered