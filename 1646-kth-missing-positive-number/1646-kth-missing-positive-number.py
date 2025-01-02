class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        expected = 1
        missing = 0
        i = 0
        while i < len(arr):
            if arr[i] == expected:
                i += 1
            else:
                missing += 1
            if missing == k:
                return expected
            expected += 1
        return (k - missing) + arr[-1]