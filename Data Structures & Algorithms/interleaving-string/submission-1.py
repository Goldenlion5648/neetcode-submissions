import functools
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @functools.cache
        def dp(pos1, pos2):
            if pos1 == len(s1):
                remaining = s2[pos2:]
                return s3[-len(remaining):] == remaining
            if pos2 == len(s2):
                remaining = s1[pos1:]
                return s3[-len(remaining):] == remaining
            
            ret = False
            if s1[pos1] == s3[pos1+pos2]:
                ret = dp(pos1 + 1, pos2)

            if s2[pos2] == s3[pos1+pos2]:
                ret = ret or dp(pos1, pos2 + 1)
            return ret
        if len(s1) + len(s2) != len(s3):
            return False
        return dp(0,0)




            