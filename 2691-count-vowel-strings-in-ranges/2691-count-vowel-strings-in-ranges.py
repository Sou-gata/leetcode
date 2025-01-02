class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix = [0] * (len(words) + 1)
        s = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                s += 1
            prefix[i + 1] = s
        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            ans[i] = prefix[query[1] + 1] - prefix[query[0]]
        return ans