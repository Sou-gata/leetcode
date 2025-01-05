class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx = None
        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else:
            idx = 2
        count = 0
        for item in items:
            if item[idx] == ruleValue:
                count += 1
        return count