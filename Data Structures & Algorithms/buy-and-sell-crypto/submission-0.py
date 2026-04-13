class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        sell = prices[0]
        buy = prices[0]
        for i, n in enumerate(prices):
            sell = n
            for j in range(i):
                temp = prices[j]
                buy = min(buy, temp)
            profit = max(profit, (sell-buy))
        return profit