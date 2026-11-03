class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = defaultdict(int)
        dp[-1, 0] = 1
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        for y in range(n):
            for x in range(m):
                if obstacleGrid[y][x] == 1:
                    continue
                dp[y, x] = dp[y-1, x] + dp[y, x-1]
        return dp[n-1,m-1]