class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(options, start):
            if start == len(options):
                ret.append(options.copy())
                return
            for i in range(start, len(options)):
                options[i], options[start] = options[start], options[i]
                backtrack(options, start + 1)
                options[i], options[start] = options[start], options[i]

        backtrack(nums, 0)
        return ret