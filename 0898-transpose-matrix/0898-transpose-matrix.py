class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for col in zip(*matrix):
            ans.append(list(col))
        return ans