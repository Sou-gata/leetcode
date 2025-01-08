class Solution:
    def countElements(self, nums: List[int]) -> int:
        counts = {}
        mi = nums[0]
        mx = nums[0]
        for num in nums:
            counts[num] = counts.setdefault(num, 0) + 1
            if num > mx:
                mx = num
            if num < mi:
                mi = num
        if mi == mx:
            return 0
        return len(nums) - counts[mi] - counts[mx] 