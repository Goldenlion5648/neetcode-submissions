class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        for stair in range(n):
            for jump in [1, 2]:
                if stair + jump > n:
                    break
                dp[stair + jump] += dp[stair]
        return dp[n]