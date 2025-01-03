class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        full_sum = sum(nums)
        prefix_sum = 0
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            if prefix_sum >= full_sum - prefix_sum:
                count += 1
        return count