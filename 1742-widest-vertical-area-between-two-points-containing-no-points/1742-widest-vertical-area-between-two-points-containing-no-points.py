class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = len(points)
        xcoords = [0] * l
        for i in range(l):
            xcoords[i] = points[i][0]
        xcoords.sort()
        mx = 0
        for i in range(1, len(xcoords)):
            d = xcoords[i] - xcoords[i - 1]
            if d > mx:
                mx = d
        return mx