class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_poses = {}
        for i in range(len(nums)):
            if nums[i] in nums_to_poses and target - nums[i] == nums[i]:
                return [nums_to_poses[nums[i]], i]
            comp = target - nums[i]
            if comp in nums_to_poses:
                return [nums_to_poses[comp], i]
            nums_to_poses[nums[i]] = i