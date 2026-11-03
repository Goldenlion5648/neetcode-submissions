class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        fringe = deque()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    fringe.append((0, y, x))
                    grid[y][x] = inf

        adj = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        while fringe:
            steps, y, x = fringe.popleft()
            if grid[y][x] != inf:
                continue
            grid[y][x] = steps
            
            for dy, dx in adj:
                new_y = y + dy
                new_x = x + dx
                if new_y in range(len(grid)) and new_x in range(len(grid[0])):
                    fringe.append((steps + 1, y + dy, x + dx))
            








            
            
