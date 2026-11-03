class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        def find(is_right):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if is_right:
                    if nums[mid] <= target:
                        lo = mid + 1
                    else:
                        hi = mid
                else:
                    if nums[mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid
            if is_right:
                lo -= 1
            print(lo, is_right)
            if lo not in range(len(nums)):
                return -1
            if nums[lo] != target:
                return -1
            return lo
        return [find(False), find(True)]
        
        
