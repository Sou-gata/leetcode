class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        total = sum(arr)
        for windowSize in range(3, l + 1, 2):
            prefixSum = 0
            for i in range(windowSize):
                prefixSum += arr[i]
            total += prefixSum
            for i in range(1, l - windowSize + 1):
                prefixSum += (arr[i + windowSize - 1] - arr[i - 1])
                total += prefixSum
        return total