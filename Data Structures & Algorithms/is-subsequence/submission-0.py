class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos1 = 0
        pos2 = 0
        while pos1 < len(s) and pos2 < len(t):
            if s[pos1] == t[pos2]:
                pos1 += 1
            pos2 += 1
        return pos1 == len(s)