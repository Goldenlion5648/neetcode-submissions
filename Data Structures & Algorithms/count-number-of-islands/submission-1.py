class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        adj = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]
        def dfs(start_y, start_x):
            grid[start_y][start_x] = "0"
            for dy, dx in adj:
                new_y = start_y + dy
                new_x = start_x + dx
                if new_y in range(len(grid)) and new_x in range(len(grid[0])):
                    if grid[new_y][new_x] == "1":
                        dfs(new_y, new_x)

        ret = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    ret += 1
                    dfs(y, x)
        return ret
