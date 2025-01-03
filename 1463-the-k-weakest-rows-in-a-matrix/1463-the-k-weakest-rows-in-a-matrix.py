class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_power = []
        for i in range(len(mat)):
            row_power.append({"power": mat[i].count(1)*100 + i, "index": i})
        row_power.sort(key=lambda x: x["power"])
        print(row_power)
        ans = [-1] * k
        for i in range(k):
            ans[i] = row_power[i]["index"]
        return ans