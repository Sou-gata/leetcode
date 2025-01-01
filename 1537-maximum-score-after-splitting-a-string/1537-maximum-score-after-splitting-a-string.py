class Solution:
    def maxScore(self, s: str) -> int:
        sumOne = s.count("1")
        sumZero = 0
        max_score = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                sumZero += 1
            else:
                sumZero -= 1
            max_score = max(max_score, sumZero + sumOne)
        return max_score