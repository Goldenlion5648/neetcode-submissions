class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        og_y_dim = len(matrix)
        og_x_dim = len(matrix[0])
        ret = [[0]*og_y_dim for _ in range(og_x_dim)]
        for y in range(og_y_dim):
            for x in range(og_x_dim):
                ret[x][y] = matrix[y][x]
        return ret