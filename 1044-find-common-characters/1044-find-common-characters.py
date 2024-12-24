class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        l = len(words)
        if l == 1:
            return list(words[0])
        # find common in 0 and 1
        c = []
        for i in set(words[0]):
            if i in set(words[1]):
                for j in range(min(words[0].count(i), words[1].count(i))):
                    c.append(i)
        if l == 2:
            return list(c)
        for i in range(2, l):
            for j in range(len(c) - 1, -1, -1):
                if c.count(c[j]) > words[i].count(c[j]):
                    c.pop(j)
        return c
