class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)
        st = ""
        i = 0
        j = 0
        while i < sl and j < tl:
            if s[i] == t[j]:
                st += t[j]
                i += 1
            j += 1
        return st == s