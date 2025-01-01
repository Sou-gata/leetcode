class Solution:
    def findEnd(self, key, table):
        if key in table:
            return self.findEnd(table[key], table)
        else:
            return key

    def destCity(self, paths: list[list[str]]) -> str:
        table = {}
        for path in paths:
            table[path[0]] = path[1]
        return self.findEnd(paths[0][0], table)
        