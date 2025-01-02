class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -(k + 1)
        for i in range(len(nums)):
            if nums[i] == 1:
                distance = i - prev - 1
                if distance < k:
                    return False
                prev = i
        return True