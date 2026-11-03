import functools
class Solution:
    def integerBreak(self, n: int) -> int:
        @functools.cache
        def helper(n):
            ret = n
            for i in range(1, n - 1):
                ret = max(ret, i * helper(n-i))
            return ret
        if n <= 3:
            return n-1
        return helper(n)
        
