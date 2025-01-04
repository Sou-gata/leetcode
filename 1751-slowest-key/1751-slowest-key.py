class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest = releaseTimes[0]
        key = ord(keysPressed[0])
        for i in range(1, len(keysPressed)):
            press = releaseTimes[i] - releaseTimes[i - 1]
            if press > longest or press == longest and ord(keysPressed[i]) > key:
                longest = press
                key = ord(keysPressed[i])
        return chr(key)
