import functools
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @functools.cache
        def dfs(s_pos, t_pos):
            if t_pos == len(t):
                return 1
            if s_pos >= len(s):
                return 0
            ret = 0
            if s[s_pos] == t[t_pos]:
                ret += dfs(s_pos + 1, t_pos + 1)
            ret += dfs(s_pos+1, t_pos)
            return ret
        return dfs(0, 0)
