class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        min_len = min(l1, l2)
        new_str = ""
        for i in range(min_len):
            new_str += word1[i] + word2[i]
        if l1 > min_len:
            new_str += word1[min_len:]
        if l2 > min_len:
            new_str += word2[min_len:]
        return new_str