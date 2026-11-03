class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_poses = defaultdict(set)
        for i in range(len(nums)):
            nums_to_poses[nums[i]].add(i)
        for i in range(len(nums)):
            cur = target - nums[i]
            if cur in nums_to_poses:
                if cur == nums[i]:
                    if len(nums_to_poses[cur]) > 1:
                        nums_to_poses[cur].discard(i)
                        other = nums_to_poses[cur].pop()
                        return [i, other]
                else:
                    return [i, nums_to_poses[cur].pop()]