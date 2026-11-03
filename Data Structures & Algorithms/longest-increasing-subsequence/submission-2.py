import functools
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @functools.cache
        def dp(pos):
            if pos == len(nums):
                return 0
            best = 1
            for i in range(pos + 1,len(nums)):
                if nums[i] > nums[pos]:
                    best = max(best, 1 + dp(i))
            return best 

        ret = 0
        for i in range(len(nums)):
            ret = max(ret, dp(i))
        return ret