
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        left_hi = height[left]
        right_hi = height[right]
        ret = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_hi = max(left_hi, height[left])
                ret += left_hi - height[left]
            else:
                right -= 1
                right_hi = max(right_hi, height[right])
                ret += right_hi - height[right]
        return ret




