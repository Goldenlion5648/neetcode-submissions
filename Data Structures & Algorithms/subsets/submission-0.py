import functools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(mask):
            if not mask:
                return []
            ret = []
            for i in range(len(nums)-1, -1, -1):
                if mask & (1 << i):
                    ret.append(nums[i])
            return ret
        answer = []
        for mask in range(0, 2 ** len(nums)):
            answer.append(dfs(mask))
                
        return answer
