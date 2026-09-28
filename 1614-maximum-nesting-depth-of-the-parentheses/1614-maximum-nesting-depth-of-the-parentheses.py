class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        ans = 0

        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
                ans = max(ans,depth)

            elif s[i] == ")":
                depth -= 1
        return ans