class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = sum(accounts[0])
        for i in range(1, len(accounts)):
            s = sum(accounts[i])
            if s > mx:
                mx = s
        return mx