class Solution:
    def trimMean(self, arr: List[int]) -> float:
        l = len(arr)
        remove_len = l // 20
        arr.sort()
        s = sum(arr[remove_len:l - remove_len])
        return s / (l - 2 * remove_len)