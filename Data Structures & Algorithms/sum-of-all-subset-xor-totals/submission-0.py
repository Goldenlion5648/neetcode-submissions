class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        ret = 0
        def backtrack(pos, xor_total):
            nonlocal ret
            if pos == len(nums):
                ret += xor_total
                return
            backtrack(pos + 1, xor_total ^ nums[pos])
            backtrack(pos + 1, xor_total)
        backtrack(0, 0)
        return ret