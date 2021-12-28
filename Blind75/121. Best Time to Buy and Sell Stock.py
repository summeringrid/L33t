class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        buy, sell = 0, 1
        maxProfit = 0

        while sell < N:
            if prices[buy] < prices[sell]:
                currentProfit = prices[sell] - prices[buy]
                maxProfit = max(currentProfit, maxProfit)
            else:
                buy = sell
            sell += 1
        return maxProfit
        # Time = O(N)
        # Space = O(1)