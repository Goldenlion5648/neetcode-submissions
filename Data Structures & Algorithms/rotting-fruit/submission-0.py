class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bad = set()
        good_fruit_count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    bad.add((y, x))
                if grid[y][x] == 1:
                    good_fruit_count += 1
        new_bad = set()
        adj = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
        step = 0
        while len(bad):
            found_fruit = False
            new_bad = set()
            for y, x in bad:
                for dy, dx in adj:
                    new_y = dy + y
                    new_x = dx + x
                    if new_y in range(len(grid)) and new_x in range(len(grid[0])):
                        if grid[new_y][new_x] == 1:
                            found_fruit = True
                            new_bad.add((new_y, new_x))
                            grid[new_y][new_x] = 2
                            good_fruit_count -= 1
            if found_fruit:
                step += 1
            bad = new_bad
        if good_fruit_count > 0:
            return -1
        return step

            