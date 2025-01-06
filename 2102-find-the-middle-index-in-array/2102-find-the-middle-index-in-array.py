class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        rightSum = sum(nums)
        leftSum = 0
        for i in range(n):
            if rightSum - nums[i] == leftSum:
                return i
            rightSum -= nums[i]
            leftSum += nums[i]
        return -1