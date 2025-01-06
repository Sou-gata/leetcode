class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        answer = 0
        for num in nums:
            compliment = k + num
            if compliment in counts:
                answer += counts[compliment]
        return answer