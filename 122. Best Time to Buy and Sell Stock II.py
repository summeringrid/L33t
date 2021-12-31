class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 1st try
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            if price > buy:
                profit += (price - buy)
                buy = float('inf')
            else:
                buy = price
        return profit
        # ❌ haven't consider one situation: [1,2,4] buy at 1 sell at 4

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # Time = O(n)