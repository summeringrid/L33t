class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # direction DP

        if len(prices) <= 1:
            return 0

        length = len(prices)
        left_min = prices[0]
        right_max = prices[-1]

        left_profits = [0] * length
        right_profits = [0] * (length + 1)

        for l in range(1, length):
            left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - l - 1
            right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])

        return max_profit


