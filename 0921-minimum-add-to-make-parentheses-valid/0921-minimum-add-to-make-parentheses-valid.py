class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        start = 0
        ans = 0

        for i in s:
            if i == '(':
                start += 1
            else:
                if start > 0:
                    start -= 1
                else:
                    ans += 1
        return ans + start