class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        ret = []
        cur = []
        def dfs():
            if len(cur) == len(nums):
                ret.append(cur.copy())
                return 
            
            for x in counts:
                if counts[x] > 0:
                    counts[x] -= 1
                    cur.append(x)
                    dfs()
                    cur.pop()
                    counts[x] += 1

        dfs()
        return ret
                