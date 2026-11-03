'''
options:
time: naive n^3
space: O(1)

make a set of the elements
double for loop and check complement in set
time: n^2
space: O(n)

sort()
go through the sorted list and use two pointers (one on the left, one on right)

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_to_indexes = defaultdict(set)
        for i, num in enumerate(nums):
            num_to_indexes[num].add(i)

        ret = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                cur = -(nums[i] + nums[j])
                if cur in num_to_indexes:
                    temp = {i, j}
                    for third in (num_to_indexes[cur]-temp):
                        ret.add(tuple(sorted([nums[i], nums[j], nums[third]])))
        ret = [list(x) for x in ret]
        return ret
                






















