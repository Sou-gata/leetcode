class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        sm = 51
        l = len(nums)
        for i in range(l // 2):
            avg = (nums[i] + nums[l - i - 1]) / 2
            if sm > avg:
                sm = avg
        return sm
            