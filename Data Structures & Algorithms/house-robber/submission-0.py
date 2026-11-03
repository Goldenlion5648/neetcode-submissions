from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dp(pos):
            if pos >= len(nums):
                return 0
            return max(
                nums[pos] + dp(pos + 2),
                nums[pos] + dp(pos + 3),
                dp(pos + 1),
            )
        return dp(0)