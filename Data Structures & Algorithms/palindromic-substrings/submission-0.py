class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        for center in range(len(s)):
            for i in range(len(s)):
                if center - i < 0 or center + i >= len(s):
                    break
                if s[center - i] == s[center + i]:
                    ret += 1
                else:
                    break
            for i in range(len(s)-1):
                if center - i < 0 or center + i + 1 >= len(s):
                    break
                if s[center - i] == s[center + i + 1]:
                    ret += 1
                else:
                    break
        return ret
                