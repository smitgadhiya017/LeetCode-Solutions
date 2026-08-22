class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        sum1 = 0
        product = 1
        while temp:
            d = temp % 10
            sum1 += d
            product *= d
            temp //= 10
        
        total = 0
        total = sum1 + product
        return n % total == 0