class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        richest = 0
        l,r = 0,1

        while r < len(prices):
            profit = prices[r] - prices[l]
            richest = max(profit, richest)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return richest
