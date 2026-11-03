class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = defaultdict(bool)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    dp[i+len(word)] = True
        return dp[len(s)]