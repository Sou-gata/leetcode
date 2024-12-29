class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        nums.reverse()
        for i in range(k // 2):
            t = nums[i]
            nums[i] = nums[k - i - 1]
            nums[k - i - 1] = t
        for i in range((l - k) // 2):
            t = nums[i + k]
            nums[i + k] = nums[l - i - 1]
            nums[l - i - 1] = t