class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        invalid = 0
        for word in words:
            for c in word:
                if c not in allowed:
                    invalid += 1
                    break
        return len(words) - invalid