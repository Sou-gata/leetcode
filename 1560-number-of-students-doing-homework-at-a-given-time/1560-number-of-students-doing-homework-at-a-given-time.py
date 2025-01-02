class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        l = len(startTime)
        total = 0
        for i in range(l):
            if startTime[i] <= queryTime <= endTime[i]:
                total += 1
        return total