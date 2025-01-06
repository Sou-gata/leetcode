class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mi = float('inf')
        for i in range(len(nums) - k + 1):
            d = nums[i + k - 1] - nums[i]
            if d < mi:
                mi = d
        return mi