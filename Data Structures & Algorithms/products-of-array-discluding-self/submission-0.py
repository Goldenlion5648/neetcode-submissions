'''
        2    5   6
pre     2   10  60 
suf     60  30   6 
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = defaultdict(lambda : 1)
        suffix = defaultdict(lambda : 1)
        for i in range(len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]
        ret = [0]*len(nums)
        for i in range(len(nums)):
            ret[i] = suffix[i+1] * prefix[i-1]
        return ret
