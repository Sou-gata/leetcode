class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        minLen = length/2
        uNums = set(nums)

        for i in uNums:
            count = nums.count(i)
            if count > minLen:
                return i
        return None