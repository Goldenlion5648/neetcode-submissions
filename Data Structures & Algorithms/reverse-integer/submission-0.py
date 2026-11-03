class Solution:
    def reverse(self, x: int) -> int:
        seen = []
        was_neg = x < 0
        x = abs(x)
        while x:
            seen.append(x % 10)
            x //= 10
        ret = 0
        for x in seen:
            ret = (ret * 10) + x
        if was_neg:
            ret *= -1
        cap = 1 << 31
        if ret not in range(-cap, cap):
            return 0
        return ret