class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            p = prices[i] - buy
            profit =max(profit,p)
        return profit