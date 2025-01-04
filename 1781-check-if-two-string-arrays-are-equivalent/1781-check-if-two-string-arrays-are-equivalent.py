class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if word1[0][0] != word2[0][0]:
            return False
        return "".join(word1) == "".join(word2)
