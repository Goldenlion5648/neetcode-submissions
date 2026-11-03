import functools
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @functools.cache
        def dp(index, total):
            if index == len(nums):
                return int(total == target)
            ret = dp(index + 1, total + nums[index]) + dp(index + 1, total - nums[index]) 
            return ret
        return dp(0, 0)