class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = defaultdict(lambda : math.inf)
        dp[0] = 0
        dp[1] = 0
        for i in range(len(cost)):
            for jump in [1, 2]:
                dp[i + jump] = min(dp[i + jump], dp[i] + cost[i])
        return dp[len(cost)]

