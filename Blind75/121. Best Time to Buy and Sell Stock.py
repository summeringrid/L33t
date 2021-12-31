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


        # Approach II
        buy = princes[0]
        profit = 0

        for price in prices[1:]:
            buy = min(buy, price)
            sell = price
            profit = max(profit, sell - buy)
        return profit

        # Time = O(n*k), n = len(prices), k = transit num (here is 1)

        # 隔板法（python will get a TLE
