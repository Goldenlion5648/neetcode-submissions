class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhat(p1, p2):
            return sum(abs(coord1 - coord2) for coord1, coord2 in zip(p1, p2))
        connected = {0}
        distances = []
        newest = 0
        ret = 0
        while len(connected) < len(points):
            for i in range(len(points)):
                if i == newest or i in connected:
                    continue
                heapq.heappush(distances, 
                    (manhat(points[newest], points[i]), newest, i)
                )
        
            while distances:
                dist, old_new, new_new = heapq.heappop(distances)
                if new_new in connected:
                    continue
                ret += dist
                # connected.add(old_new)
                connected.add(new_new)
                newest = new_new
                break
        return ret