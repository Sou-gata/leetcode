class Solution:
    def findHeight(self, one: int, two: int) -> int:
        height = 0
        while True:
            need = height + 1
            if need % 2 == 1:
                if one >= need:
                    one -= need
                    height += 1
                else:
                    break
            else:
                if two >= need:
                    two -= need
                    height += 1
                else:
                    break
        return height

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        a = self.findHeight(red, blue)
        b = self.findHeight(blue, red)
        return max(a, b)