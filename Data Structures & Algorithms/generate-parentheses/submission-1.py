class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def dfs(current, depth):
            if len(current) == n * 2:
                if depth == 0:
                    ret.append("".join(current))
                return
            if depth != 0:
                current.append(")")
                dfs(current, depth - 1)
                current.pop()
            current.append("(")
            dfs(current, depth + 1)
            current.pop()
        dfs([], 0)
        return ret
            