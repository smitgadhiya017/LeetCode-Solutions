class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]

            maxProfit = max(maxProfit, prices[i] - minPrice)
        
        return maxProfit