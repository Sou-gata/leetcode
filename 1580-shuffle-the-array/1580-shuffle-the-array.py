class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # l = len(nums)
        # ans = [0] * l
        # for i in range(0, l, 2):
        #     ans[i] = nums[i // 2]
        #     ans[i + 1] = nums[(i + l) // 2]
        # return ans
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans