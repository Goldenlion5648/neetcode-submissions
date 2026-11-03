class Solution:
    def canJump(self, nums: List[int]) -> bool:
        highest = nums[0]
        for i in range(len(nums)):
            if i > highest:
                return False
            highest = max(highest, nums[i] + i)
        return True