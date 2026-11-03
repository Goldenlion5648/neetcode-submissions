class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(arr):
            if len(arr) <= 1:
                return [arr]
            ret = []
            for i in range(len(arr)):
                # if arr[i] == arr[i-1]:
                #     continue
                next = arr[:i] + arr[i+1:]
                for found in dfs(next):
                    ret.append([arr[i]] + found)
            return ret
        seen = set()
        for found in dfs(nums):
            seen.add(tuple(found))
        ret = [list(x) for x in seen]

        return ret
                