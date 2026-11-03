class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_time_with_speed(k):
            ret = 0
            for i in range(len(piles)):
                ret += math.ceil(piles[i] / k)
            return ret
        
        lo = 1
        hi = max(piles)
        best = hi
        while lo < hi:
            mid = (lo + hi) // 2
            time_taken = get_time_with_speed(mid)
            if time_taken <= h:
                best = mid
                hi = mid
            else:
                lo = mid + 1
        return best