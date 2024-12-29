class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = ""
        prev = chars[0]
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == prev:
                count+= 1
            else:
                if count != 1:
                    ans += (prev + str(count))
                else:
                    ans += prev
                prev = chars[i]
                count = 1
        if count != 1:
            ans += (prev + str(count))
        else:
            ans += prev
        for i in range(len(ans)):
            chars[i]= ans[i]
        return len(ans)