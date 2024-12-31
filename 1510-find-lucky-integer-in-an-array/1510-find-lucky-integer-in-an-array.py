class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # freq_map= {}
        # for i in arr:
        #     if i not in freq_map:
        #         freq_map[i] = 1
        #     else:
        #         freq_map[i] += 1
        # ans = []
        # for i in set(arr):
        #     if freq_map[i] == i:
        #         ans.append(i)
        # if ans:
        #     return max(ans)
        # else:
        #     return -1
        ans = -1
        for i in set(arr):
            if i == arr.count(i) and i > ans:
                ans = i
        return ans