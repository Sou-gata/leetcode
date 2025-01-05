class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mi = 10001
        for i in range(len(nums)):
            if nums[i] == target:
                d = abs(i - start)
                if d < mi:
                    mi = d
        return mi