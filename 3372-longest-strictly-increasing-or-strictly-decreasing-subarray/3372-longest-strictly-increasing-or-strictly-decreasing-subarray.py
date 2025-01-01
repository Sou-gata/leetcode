class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        inc_len = 1
        dec_len = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < prev:
                inc_len = 1
                dec_len += 1
            elif nums[i] > prev:
                inc_len += 1
                dec_len = 1
            else:
                inc_len = 1
                dec_len = 1
            if inc_len > inc:
                inc = inc_len
            if dec_len > dec:
                dec = dec_len
            prev = nums[i]
        return max(inc, dec)