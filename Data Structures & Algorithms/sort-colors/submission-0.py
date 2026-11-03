class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0]*3
        for ele in nums:
            counts[ele] += 1
        counts_index = 0
        nums_index = 0
        while nums_index < len(nums) and counts_index < len(counts):
            if counts[counts_index] > 0:
                nums[nums_index] = counts_index
                counts[counts_index] -= 1
                nums_index += 1
            else:
                counts_index += 1
        