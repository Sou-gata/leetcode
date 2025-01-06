class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = {}
        for s in arr:
            counts[s] = counts.setdefault(s, 0) + 1
        c = 0
        for s in arr:
            if counts[s] == 1:
                c += 1
                if c == k:
                    return s
        return ""