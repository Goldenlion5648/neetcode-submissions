import functools
import string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        @functools.cache
        def conform_to(letter, pos, k):
            if pos == len(s):
                return 0
            if k == 0:
                extra = 0
                while pos < len(s) and s[pos] == letter:
                    extra += 1
                    pos += 1
                return extra

            if s[pos] == letter:
                return conform_to(letter, pos+1, k) + 1
            
            return conform_to(letter, pos+1, k-1) + 1

        ret = 0
        for letter in string.ascii_uppercase:
            for i in range(len(s)):
                ret = max(ret, conform_to(letter, i, k))
        return ret

