import functools
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @functools.cache
        def dp(pos):
            if pos == len(s):
                return 1
            if s[pos] == "0":
                return 0
            ret = 0
            ret += dp(pos+1)
            next_two = int(s[pos:pos+2])
            if next_two in range(10, 27) and pos + 2 <= len(s):
                ret += dp(pos+2)
            return ret
        return dp(0)