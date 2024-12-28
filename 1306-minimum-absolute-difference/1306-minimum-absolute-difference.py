class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        l = len(arr)
        ans = []
        mindiff = abs(arr[0] - arr[1])
        for i in range(1, l - 1):
            d = abs(arr[i] - arr[i + 1])
            if d < mindiff:
                mindiff = d
        for i in range(l - 1):
            d = abs(arr[i] - arr[i + 1])
            if d == mindiff:
                ans.append([arr[i], arr[i + 1]])
        return ans