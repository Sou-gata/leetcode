class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        prev = 0
        longest = 0
        ans = -1
        for i, event in enumerate(events):
            t = event[1] - prev
            if t > longest:
                longest = t
                ans = event[0]
            elif t == longest:
                ans = min(ans, event[0])
            prev = event[1]
        return ans