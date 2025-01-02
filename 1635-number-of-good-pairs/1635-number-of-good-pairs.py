class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        total = 0
        for i in counts.keys():
            count = counts[i]
            if counts[i] >= 2:
                n = (count * (count - 1)) // 2
                total += n
        return total
        