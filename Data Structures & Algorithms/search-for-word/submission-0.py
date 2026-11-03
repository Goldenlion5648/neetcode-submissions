class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        adj = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]
        def dfs(y, x, index):
            if index == len(word):
                return True
            if y not in range(len(board)) or x not in range(len(board[0])):
                return False
            if board[y][x] == word[index]:
                board[y][x] = "#"
                for dy, dx in adj:
                    if dfs(y + dy, x + dx, index + 1):
                        return True
                board[y][x] = word[index]
            return False
            
        for y in range(len(board)):
            for x in range(len(board[0])):
                if dfs(y, x, 0):
                    return True
        return False
