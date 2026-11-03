class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [math.inf for _ in range(len(cost) + 1)]
        dp[0] = 0
        dp[1] = 0
        for i in range(len(cost)):
            for jump in [1, 2]:
                if i + jump < len(dp):
                    dp[i + jump] = min(dp[i + jump], dp[i] + cost[i])
        return dp[len(cost)]

