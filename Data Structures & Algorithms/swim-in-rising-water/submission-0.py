class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        fringe = [(grid[0][0], (0,0))]
        heapq.heapify(fringe)
        seen = {(0,0)}
        adj = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        while fringe:
            highest, (y, x) = heapq.heappop(fringe)
            if (y, x) == (len(grid)-1, len(grid[0])-1):
                return highest
            
            for dy, dx in adj:
                new_y = y + dy
                new_x = x + dx
                if new_y in range(len(grid)) and new_x in range(len(grid[0])):
                    new_pos = (new_y, new_x)
                    if new_pos not in seen:
                        seen.add(new_pos)
                        heapq.heappush(fringe, (max(highest, grid[new_y][new_x]), new_pos))
        return -1