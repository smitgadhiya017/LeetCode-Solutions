class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 5:
            temp = n
            total = 0 
            while temp:
                d = temp % 10
                total += d * d
                temp //= 10
            n = total
        return n == 1