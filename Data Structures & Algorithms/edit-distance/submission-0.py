import functools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.cache
        def dp(pos1, pos2):
            if pos1 == len(word1):
                return len(word2) - pos2
            if pos2 == len(word2):
                return len(word1) - pos1
            
            if word1[pos1] == word2[pos2]:
                return dp(pos1 + 1, pos2 + 1)
            
            return 1 + min(
                dp(pos1 + 1, pos2),
                dp(pos1, pos2 + 1),
                dp(pos1 + 1, pos2 + 1),
            )
        return dp(0, 0)