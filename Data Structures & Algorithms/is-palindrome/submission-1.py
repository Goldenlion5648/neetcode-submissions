class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(x for x in s.lower() if x.isalnum())
        if not s: 
            return True
        for i in range(len(s) // 2 + 1):
            if s[i] != s[-(i + 1)]:
                return False
        return True