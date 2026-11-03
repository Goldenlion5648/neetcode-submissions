class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            pos = i
            while nums[pos] != i + 1 and nums[pos] in range(1, len(nums) + 1):
                temp = nums[nums[pos]-1]
                if temp == nums[pos]:
                    break
                nums[nums[pos]-1] = nums[i]
                nums[pos] = temp
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1
        
