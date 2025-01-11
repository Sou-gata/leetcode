class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        l = len(s)
        if l < k:
            return False
        counts = {}
        for ch in s:
            counts[ch] = counts.setdefault(ch, 0) + 1
        odd_count = 0
        for i in counts.values():
            if i % 2 == 1:
                odd_count += 1
        return odd_count <= k
