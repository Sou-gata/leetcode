class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        distance = distance + distance
        ma = max(start, destination)
        mi = min(start, destination)
        n1 = sum(distance[mi:ma])
        n2 = sum(distance[ma:mi + (len(distance) // 2)])
        return min(n1, n2)    