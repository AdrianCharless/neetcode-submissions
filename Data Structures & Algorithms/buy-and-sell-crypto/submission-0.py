class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        maxProfit = 0
        for i in range(days):
            if i == 0:
                minBuy = prices[i]
            else:
                if prices[i] <= minBuy:
                    minBuy = prices[i]
                else:
                    profit = prices[i] - minBuy
                    maxProfit = max(maxProfit, profit)
                
        return maxProfit