class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = len(s)
        arranged = [None] * l
        for i in range(l):
            arranged[indices[i]] = s[i]
        return "".join(arranged)