class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for i in words:
            if i.find(pref) == 0:
                count += 1
        return count
        