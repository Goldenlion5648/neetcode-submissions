class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        back_pos = len(nums) - 1
        k = 0
        for i in range(len(nums)):
            while nums[i] == val and back_pos > i:
                ran = True
                nums[i], nums[back_pos] = nums[back_pos], nums[i]
                back_pos -= 1
            if nums[i] != val: 
                k += 1
        return k
