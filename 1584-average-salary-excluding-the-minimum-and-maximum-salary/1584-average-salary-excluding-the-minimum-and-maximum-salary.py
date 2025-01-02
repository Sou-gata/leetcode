class Solution:
    def average(self, salary: List[int]) -> float:
        s = ma = mi = salary[0]
        l = len(salary)
        for i in range(1, l):
            if salary[i] < mi:
                mi = salary[i]
            if salary[i] > ma:
                ma = salary[i]
            s += salary[i]
        return (s - mi - ma) / (l - 2)