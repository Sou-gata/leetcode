class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rsSet = set(ransomNote)
        for i in rsSet:
            n1 = ransomNote.count(i)
            n2 = magazine.count(i)
            if n1 > n2:
                return False
        return True