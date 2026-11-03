class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        seen = []
        while temp > 0:
            seen.append(temp % 10)
            temp //= 10
        for i in range(len(seen) // 2):
            if seen[i] != seen[len(seen)-(i+1)]:
                return False
        return True
            
        