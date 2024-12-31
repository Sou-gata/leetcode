class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            ans.insert(index[i], num)
        return ans