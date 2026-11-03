class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = defaultdict(int)
        dp[-1, 0] = 1
        for y in range(n):
            for x in range(m):
                dp[y, x] = dp[y-1, x] + dp[y, x-1]
        return dp[n-1,m-1]