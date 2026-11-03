'''

AACAACCAAA
          
'''
import string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        for goal in set(s):
            rem = k
            left = 0
            right = 0
            while right < len(s):
                if s[right] != goal:
                    if rem > 0:
                        rem -= 1
                    else:
                        found = False
                        while not found:
                            if s[left] != goal:
                                found = True
                                rem += 1
                            left += 1
                        rem -= 1
                best = max(best, (right + 1) - left)
                right += 1
        return best

            
