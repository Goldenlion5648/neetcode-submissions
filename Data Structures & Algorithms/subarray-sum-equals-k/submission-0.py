class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = Counter()
        counts[0] = 1
        cur = 0
        ret = 0
        for i in range(len(nums)):
            cur += nums[i]
            if cur - k in counts:
                ret += counts[cur-k]
            counts[cur] += 1
        return ret

