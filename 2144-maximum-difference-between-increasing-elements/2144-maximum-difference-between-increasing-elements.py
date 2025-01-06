class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prefix_min = nums[0]
        max_diff = -1
        for i in range(1, len(nums)):
            if nums[i] == prefix_min:
                continue
            d = nums[i] - prefix_min
            if max_diff < d:
                max_diff = d
            if nums[i] < prefix_min:
                prefix_min = nums[i]
        return max_diff