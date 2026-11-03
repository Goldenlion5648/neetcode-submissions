from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(running_total, pos):
            if pos == len(nums):
                return int(running_total == target)
            total =  dfs(running_total + nums[pos], pos + 1)
            total += dfs(running_total - nums[pos], pos + 1)
            return total
        return dfs(0, 0)