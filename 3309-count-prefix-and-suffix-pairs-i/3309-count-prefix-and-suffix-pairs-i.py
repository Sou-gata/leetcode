class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        l = len(words)
        for i in range(l):
            for j in range(i + 1, l):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        return count