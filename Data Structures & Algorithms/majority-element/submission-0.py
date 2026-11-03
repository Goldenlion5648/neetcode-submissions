class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for x in nums:
            if x not in counts:
                counts[x] = 0
            counts[x] += 1
            if counts[x] > len(nums) // 2:
                return x
        