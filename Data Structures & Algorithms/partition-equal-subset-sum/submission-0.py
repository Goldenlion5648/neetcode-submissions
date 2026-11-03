import functools
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums)
        if goal % 2 == 1:
            return False

        @functools.cache
        def dp(left_total, pos):
            if pos == len(nums):
                return left_total == goal // 2
            
            return dp(left_total + nums[pos], pos + 1) or\
                    dp(left_total, pos + 1)
        return dp(0, 0)