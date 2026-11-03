import functools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(pos): # pos 0
            if pos == len(nums):
                ret.append(nums.copy())
                return
            for i in range(pos, len(nums)):
                nums[i], nums[pos] = nums[pos], nums[i]
                dfs(pos + 1)
                nums[i], nums[pos] = nums[pos], nums[i]

        dfs(0)
        return ret

