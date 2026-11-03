class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()
        def dp(total, values, start_pos):
            if total == target:
                ret.append(values.copy())
                return
            if total > target:
                return
            for i in range(start_pos, len(nums)):
                num = nums[i]
                values.append(num)
                dp(total + num, values, i)
                values.pop()
        dp(0, [], 0)
            
        return ret
