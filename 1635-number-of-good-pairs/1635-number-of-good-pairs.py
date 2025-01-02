class Solution:
    def fact(self, n: int) -> int:
        f = 1
        for i in range(2, n + 1):
            f *= i
        return f

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
                ncr = self.fact(count) // (2 * self.fact(count - 2))
                total += ncr
        return total
        