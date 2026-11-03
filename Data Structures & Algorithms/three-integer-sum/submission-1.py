class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total == 0:
                    ret.append([num, nums[left], nums[right]])
                    l2 = left
                    while l2 < right and nums[l2] == nums[left]:
                        l2 += 1
                    left = l2
                    
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return ret
