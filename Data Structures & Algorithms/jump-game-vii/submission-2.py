class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        hi = 0
        lo = math.inf
        for i in range(len(s)):
            if s[i] == "1":
                continue
            if i != 0 and i < lo:
                continue
            if i > hi:
                return False
            if len(s)-1 in range(i + minJump, i + maxJump + 1):
                return True
            lo = min(lo, i + minJump)
            hi = max(hi, i + maxJump)
        return False

