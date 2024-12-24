class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return int(min(len(set(candyType)), len(candyType) / 2))