class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = len(nums)
        s = 0
        ans = [0] * l
        for i in range(l):
            s += nums[i]
            ans[i] = s
        return ans