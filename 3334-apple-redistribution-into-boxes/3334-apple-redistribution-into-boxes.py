class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        s = sum(apple)
        count = 0
        for i in capacity:
            if s > 0:
                s -= i
                count += 1
            else:
                break
        return count
