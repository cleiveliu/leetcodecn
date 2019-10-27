class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        buy,sell = prices[0], None
        for price in prices:
            if price < buy:
                buy = price
            else:
                sell = price
                profit = max(profit, sell-buy)
        return profit