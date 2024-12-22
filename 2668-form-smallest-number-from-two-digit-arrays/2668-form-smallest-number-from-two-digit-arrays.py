class Solution:
    def findCommonShortest(self, nums1, nums2) -> int:
        nums1.sort()
        for i in nums1:
            if i in nums2:
                return i
        return -1
    
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        m1 = min(nums1)
        m2 = min(nums2)
        c = self.findCommonShortest(nums1, nums2)
        if c != -1:
            return c
        if m1 == m2:
            return m1
        else:
            return 10 * min(m1, m2) + max(m1, m2)