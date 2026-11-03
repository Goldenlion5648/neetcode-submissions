class Solution:
    def reverse(self, x: int) -> int:
        was_neg = x < 0
        x = abs(x)
        ret = 0
        while x:
            digit = x % 10
            x //= 10
            ret = (ret * 10) + digit
        if was_neg:
            ret *= -1
        cap = 1 << 31
        if ret not in range(-cap, cap):
            return 0
        return ret