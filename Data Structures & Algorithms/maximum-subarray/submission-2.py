class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        best = cur
        for i in range(1, len(nums)):
            if cur < 0:
                cur = nums[i]
            else:
                cur += nums[i]
            best = max(best, cur)
        return best

