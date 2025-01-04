class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        freq_arr = []
        for i in freq.keys():
            freq_arr.append([i, freq[i]])
        freq_arr.sort(key = lambda x: x[1] * 300 + (300 - x[0]))
        ans = [0] * len(nums)
        k = 0
        for num, hz in freq_arr:
            for i in range(hz):
                ans[k] = num
                k += 1
        return ans