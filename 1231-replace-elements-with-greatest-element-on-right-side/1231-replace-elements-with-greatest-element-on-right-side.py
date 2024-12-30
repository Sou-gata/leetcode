class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        for i in range(len(arr) - 1, -1, -1):
            t = mx
            if arr[i] > mx:
                mx = arr[i]
            arr[i] = t
        return arr
