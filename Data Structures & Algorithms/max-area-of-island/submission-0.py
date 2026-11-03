class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(y, x):
            if y not in range(len(grid)) or x not in range(len(grid[0])):
                return 0
            if grid[y][x] == 0:
                return 0
            grid[y][x] = 0
            ret = 1
            ret += dfs(y, x + 1)
            ret += dfs(y, x - 1)
            ret += dfs(y + 1, x)
            ret += dfs(y - 1, x)
            return ret
        best = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                best = max(best, dfs(y, x))
        return best
                