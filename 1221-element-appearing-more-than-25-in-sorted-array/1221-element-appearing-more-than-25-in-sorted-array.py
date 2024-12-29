class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # lim = len(arr) / 4
        # arrSet = set(arr)
        # for i in arrSet:
        #     c = arr.count(i)
        #     if c > lim:
        #         return i
        lim = len(arr) // 4
        for i in range(len(arr) - lim):
            if arr[i] == arr[i + lim]:
                return arr[i]