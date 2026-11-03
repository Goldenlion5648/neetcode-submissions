class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhat(p1, p2):
            return sum(abs(coord1 - coord2) for coord1, coord2 in zip(p1, p2))
        connected = [False]*len(points)
        connected[0] = True
        connected_size = 1
        distances = []
        newest = 0
        ret = 0
        while connected_size < len(points):
            for i in range(len(points)):
                if i == newest or connected[i]:
                    continue
                heapq.heappush(distances, 
                    (manhat(points[newest], points[i]), newest, i)
                )
        
            while distances:
                dist, old_new, new_new = heapq.heappop(distances)
                if connected[new_new]:
                    continue
                ret += dist
                connected[new_new] = True
                newest = new_new
                connected_size += 1
                break
        return ret