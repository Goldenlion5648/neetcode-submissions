class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ret = 0
        for x in seen:
            if x - 1 in seen:
                continue
            cur = x
            streak = 0
            while cur in seen:
                streak += 1
                cur += 1
            ret = max(ret, streak)
        return ret
