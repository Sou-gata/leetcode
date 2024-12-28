class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        for word in words:
            sw = set(word)
            isAddable = True
            for s in sw:
                n1 = word.count(s)
                n2 = chars.count(s)
                if n1 > n2:
                    isAddable = False
                    break
            if isAddable:
                total += len(word)
        return total