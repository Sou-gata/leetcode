class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        brk = []
        for i in range(len(s)):
            if stack:
                if stack[-1] == "(" and s[i] == ")":
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                brk.append(i)
                stack.append(s[i])
        if not stack:
            brk.append(len(s) - 1)
        ans = ""
        for i in range(len(brk) - 1):
            if brk[i + 1] - brk[i] > 1:
                ans += s[brk[i] + 1: brk[i + 1] - 1]
        if not stack and s[len(s) - 2] != "(":
            ans += s[len(s) - 2]
        return ans