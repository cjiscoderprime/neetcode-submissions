class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            if prices[i] > prices[i - 1]:
                profit += diff
        return profit