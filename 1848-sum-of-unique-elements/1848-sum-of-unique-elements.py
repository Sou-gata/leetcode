class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        s = 0
        for c in counts.keys():
            if counts[c] == 1:
                s += c
        return s