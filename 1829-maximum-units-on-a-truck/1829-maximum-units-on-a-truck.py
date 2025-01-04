class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        s = 0
        for boxNumber, boxVal in boxTypes:
            if truckSize - boxNumber >= 0:
                truckSize -= boxNumber
                s += boxNumber * boxVal
            else:
                s += truckSize * boxVal
                break
        return s