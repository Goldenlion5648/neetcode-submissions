class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            if left + 1 == right:
                return [nums[left]]
            if left + 2 == right:
                return [min(nums[left], nums[right-1]), max(nums[left], nums[right-1])]

            mid = (left + right) // 2
            part1 = merge(left, mid)
            part2 = merge(mid, right)
            pos1 = 0
            pos2 = 0
            ret = []
            while pos1 < len(part1) and pos2 < len(part2):
                if part1[pos1] <= part2[pos2]:
                    ret.append(part1[pos1])
                    pos1 += 1
                else:
                    ret.append(part2[pos2])
                    pos2 += 1

            for j in range(pos2, len(part2)):
                ret.append(part2[j])
            for j in range(pos1, len(part1)):
                ret.append(part1[j])
            
            return ret
        return merge(0, len(nums))



















