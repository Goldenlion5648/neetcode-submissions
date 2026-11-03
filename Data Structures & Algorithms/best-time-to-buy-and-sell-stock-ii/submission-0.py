class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        cur_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                cur_profit += prices[i] - prices[i-1]
        return cur_profit