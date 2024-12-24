class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sl = s1.split(" ") + s2.split(" ")
        set_sl = set(sl)
        ans = []
        for i in set_sl:
            c = sl.count(i)
            if not c > 1:
                ans.append(i)
        return ans
