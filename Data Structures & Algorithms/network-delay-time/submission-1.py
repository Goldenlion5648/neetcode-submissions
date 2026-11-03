from _heapq import heappush
from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G = defaultdict(lambda : defaultdict(lambda : math.inf))
        for u, v, time in times:
            G[u][v] = min(G[u][v], time)
        fringe = []
        heappush(fringe, (0, k))
        ret = 0
        seen = defaultdict(lambda : math.inf)
        while fringe:
            time_taken, cur = heapq.heappop(fringe)
            if seen[cur] <= time_taken:
                continue
            seen[cur] = time_taken
            ret = max(ret, time_taken)
            if cur not in G:
                continue
            for other in G[cur]:
                new_travel = G[cur][other]
                heapq.heappush(fringe, (time_taken + new_travel, other))
        if len(seen) != n:
            return -1
        return ret

