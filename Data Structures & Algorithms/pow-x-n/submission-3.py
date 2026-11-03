class Solution:
    def myPow(self, x: float, pow: int) -> float:
        # check is neg
        if pow == 0:
            return 1
        was_neg = pow < 0
        pow = abs(pow)
        if pow == 1:
            if was_neg:
                return 1 / x
            return x
        ret = 1
        base = x
        while pow > 0:
            if pow % 2 == 1:
                ret *= base
            pow //= 2
            base *= base
        if was_neg:
            return 1 / ret
        return ret