class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx = -1
        distance = 14143
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                d = abs(points[i][0] - x) + abs(points[i][1] - y)
                if d < distance:
                    distance = d
                    idx = i
        return idx