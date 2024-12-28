class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        setTarget = set(target)
        canFormed = 200
        for i in setTarget:
            n1 = target.count(i)
            n2 = s.count(i)
            canFormed = min(canFormed, n2 // n1)
        return canFormed