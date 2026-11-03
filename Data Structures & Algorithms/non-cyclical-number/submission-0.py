class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            temp = n
            total = 0
            while temp:
                total += (temp % 10) ** 2
                temp //= 10
            n = total
        return True