class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int ret = 0;
        for (int y = 0; y < grid.size(); y++){
            for (int x = 0; x < grid[0].size(); x++) {
                if (grid[y][x] == '1') {
                    ret += 1;
                    dfs(grid, y, x);
                }
            }
        }
        return ret;
    }
    void dfs(vector<vector<char>>& grid, int y, int x) {
        array<array<int, 2>, 4> adj = {{
            {-1, 0},
            {1, 0},
            {0, 1},
            {0, -1},
        }};
        if (grid[y][x] == '0') {
            return;
        }
        grid[y][x] = '0';
        for (const auto& [dy, dx] : adj) {
            int new_y = y + dy;
            int new_x = x + dx;
            if (
                new_y >= 0 && new_y < grid.size() &&
                new_x >= 0 && new_x < grid[0].size()
            ) {
                dfs(grid, new_y, new_x);
            }
        }

    }

};
