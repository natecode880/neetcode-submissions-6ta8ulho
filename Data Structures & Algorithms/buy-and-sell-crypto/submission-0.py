class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > best_profit:
                best_profit = profit

        return best_profit