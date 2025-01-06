class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # s1 = set()
        # s2 = set()
        # s3 = set()
        # s = set()
        # result = set()
        # for i in nums1:
        #     s1.add(i)
        #     s.add(i)
        # for i in nums2:
        #     s2.add(i)
        #     s.add(i)
        # for i in nums3:
        #     s3.add(i)
        #     s.add(i)
        # for i in s:
        #     if ((i in s1) and (i in s2)) or ((i in s2) and (i in s3)) or ((i in s3) and (i in s1)):
        #         result.add(i)
        # return list(result)
        s1=set(nums1)
        s2=set(nums2)
        s3=set(nums3)
        return list(s1.intersection(s2).union(s2.intersection(s3)).union(s1.intersection(s3)))