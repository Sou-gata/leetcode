class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        min_sum = 0
        nums_set = list(set(nums))
        nums_set.sort()
        for i in nums_set:
            if k - i < 0:
                break
            else:
                k += 1
                min_sum += i
        print(k)
        return ((k * (k + 1)) // 2) - min_sum