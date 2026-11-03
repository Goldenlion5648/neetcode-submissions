class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for y in range(m):
            for x in range(n):
                if x == 0 and y == 0:
                    continue
                above = 0 if y == 0 else dp[y-1][x]
                left = 0 if x == 0 else dp[y][x-1]
                dp[y][x] = above + left
        return dp[-1][-1]