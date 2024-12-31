class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        hash_map = {}
        for i in range(len(sorted_list)):
            if sorted_list[i] not in hash_map:
                hash_map[sorted_list[i]] = i
        return [hash_map[num] for num in nums]