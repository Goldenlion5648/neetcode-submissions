class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, s) for pos, s in zip(position, speed)]
        pairs.sort()
        pos = len(pairs) - 2
        ret = 1
        def get_time(index):
            return (target - pairs[index][0]) / pairs[index][1]
        slowest_index = pos + 1
        while pos >= 0:
            prev_time = get_time(slowest_index)
            cur_time =  get_time(pos)
            if cur_time > prev_time:
                ret += 1
                slowest_index = pos
            pos -= 1
        return ret

