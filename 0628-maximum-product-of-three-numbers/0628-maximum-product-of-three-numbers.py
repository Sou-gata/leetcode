class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n1 = nums[0] * nums[1] * nums[-1]  # n-n-p
        n2 = nums[-1] * nums[-2] * nums[-3]  # p-p-p / n-n-n
        return max(n1, n2)