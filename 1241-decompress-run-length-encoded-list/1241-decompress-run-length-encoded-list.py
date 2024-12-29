class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = []
        for i in range(0, l, 2):
            freq = nums[i]
            ans += [nums[i+1]]*freq
        return ans