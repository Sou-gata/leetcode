class Solution:
        def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            nxt = {}
            stack = []
            for num in nums2:
                while stack and stack[-1] < num:
                    nxt[stack.pop()] = num
                stack.append(num)
            ans = [-1] * len(nums1)
            for i in range(len(nums1)):
                n = nums1[i]
                if n in nxt:
                    ans[i] = nxt[n]
            return ans