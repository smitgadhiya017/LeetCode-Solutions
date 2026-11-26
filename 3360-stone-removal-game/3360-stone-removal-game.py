class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        ans = True

        while n >= remove:
            n -= remove
            remove -= 1
            ans = not ans

        return not ans