class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix = [0] * len(words)
        s = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                s += 1
            prefix[i] = s
        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            prev = query[0] - 1
            prev = 0 if prev < 0 else prefix[prev]
            s = query[1]
            ans[i] = prefix[s] - prev
        return ans
