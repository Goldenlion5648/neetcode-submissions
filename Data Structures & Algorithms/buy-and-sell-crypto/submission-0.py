class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        lo = math.inf
        for price in prices:
            best = max(best, price - lo)
            lo = min(lo, price)
        return best
