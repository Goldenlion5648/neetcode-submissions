class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        # coins.sort()
        for i in range(len(dp)):
            for coin in coins:
                if i+coin >= len(dp):
                    continue
                dp[i+coin] = min(dp[i+coin], dp[i] + 1)
        if dp[amount] == math.inf:
            return -1
        return dp[amount]


        