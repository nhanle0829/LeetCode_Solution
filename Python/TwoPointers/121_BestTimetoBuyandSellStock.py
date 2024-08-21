class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = float("inf")
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                profit = max(profit, price - lowest)

        return profit
